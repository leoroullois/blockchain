from flask import Flask, jsonify
from blockchain.Node import Node
from blockchain.Blockchain import Blockchain

import threading
from queue import Queue


class Api:
    def __init__(
        self,
        blockchain: list[Blockchain],
        nodes: list[Node],
        host: str = "0.0.0.0",
        port: int = 5000,
    ):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.blockchain = blockchain
        self.nodes = nodes

    def worker(self, node: Node, q: Queue):
        nonce = node.mine_block()
        q.put(nonce)
        return nonce

    def mine_block(self):
        q = Queue()
        t = [
            threading.Thread(target=self.worker, args=(node, q), daemon=False)
            for node in self.nodes
        ]

        for thread in t:
            thread.start()

        for thread in t:
            thread.join()

        nonce_set = list(set(q.queue))
        n = len(nonce_set)
        if n == 0:
            response = {
                "success": False,
                "message": "No nonce found. Block not mined.",
            }
        elif n == 1:
            blockchain = self.blockchain

            previous_block = blockchain.print_previous_block()
            previous_hash = previous_block.hash()
            block = blockchain.create_block(q.get(), previous_hash)
            response = {
                "message": "A block is MINED",
                "success": True,
                **block.get_block(),
            }
        else:
            response = {
                "success": False,
                "message": "More than one nonce found. Block not mined.",
            }

        return jsonify(response), 200

    def display_chain(self):
        chain = self.blockchain.get_blockchain()
        response = {"chain": chain, "length": len(self.blockchain.chain)}
        return jsonify(response), 200


    def valid(self):
        valid = self.blockchain.chain_valid(self.blockchain.chain)

        if valid:
            response = {"message": "The Blockchain is valid."}
        else:
            response = {"message": "The Blockchain is not valid."}
        return jsonify(response), 200

    def create_fake_block(self):
        self.blockchain.create_fake_block()
        response = {"message": "Fake block created."}
        return jsonify(response), 200

    def start(self):
        app = self.app

        @app.route("/mine_block", methods=["GET"])
        def mine_block():
            return self.mine_block()

        @app.route("/get_chain", methods=["GET"])
        def display_chain():
            return self.display_chain()

        @app.route("/valid", methods=["GET"])
        def valid():
            return self.valid()

        @app.route("/create-fake-block", methods=["GET"])
        def create_fake_block():
            return self.create_fake_block()

        self.app.run(host=self.host, port=self.port)
