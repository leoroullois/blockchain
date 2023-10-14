import datetime
import threading

from flask import Flask, jsonify, request
from queue import Queue

from blockchain.Node import Node
from blockchain.Blockchain import Blockchain


class Api:
    def __init__(
        self,
        blockchain: Blockchain,
        nodes: list[Node],
        host: str = "0.0.0.0",
        port: int = 5000,
    ):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.blockchain = blockchain
        self.nodes = nodes

    def worker(self, node: Node, data: str, timestamp: str, q: Queue):
        nonce = node.mine_block(data, timestamp)
        if q.empty():
            q.put(nonce)
        return nonce

    def start(self):
        app = self.app

        @app.route("/mine_block", methods=["POST"])
        def mine_block():
            data = request.json["data"]
            timestamp = str(datetime.datetime.now())
            q = Queue()
            t = [
                threading.Thread(
                    target=self.worker, args=(node, data, timestamp, q), daemon=False
                )
                for node in self.nodes
            ]

            for thread in t:
                thread.start()

            for thread in t:
                thread.join()

            if q.empty():
                response = {
                    "success": False,
                    "message": "No nonce found. Block not mined.",
                }
            else:
                blockchain = self.blockchain

                previous_block = blockchain.print_previous_block()
                previous_hash = previous_block.hash()

                block = blockchain.create_block(q.get(), previous_hash, data, timestamp)
                response = {
                    "message": "A block is MINED",
                    "success": True,
                    **block.get_block(),
                    "hash": block.hash(),
                }

            return jsonify(response), 200

        @app.route("/get_chain", methods=["GET"])
        def display_chain():
            chain = self.blockchain.get_blockchain()
            response = {"chain": chain, "length": len(self.blockchain.chain)}
            return jsonify(response), 200

        @app.route("/valid", methods=["GET"])
        def valid():
            valid = self.blockchain.chain_valid(self.blockchain.chain)
            return jsonify({"success": True, "valid": valid}), 200

        @app.route("/create-fake-block", methods=["GET"])
        def create_fake_block():
            self.blockchain.create_fake_block()
            response = {"message": "Fake block created."}
            return jsonify(response), 200

        @app.route("/peers", methods=["GET"])
        def peers():
            return jsonify({"success": True, "nbNodes": len(self.nodes)}), 200

        self.app.run(host=self.host, port=self.port)
