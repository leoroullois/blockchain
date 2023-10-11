import datetime
import hashlib

from blockchain.Block import Block

class Blockchain:
    # This function is created
    # to create the very first
    # block and set its hash to "0"
    def __init__(self):
        self.chain: list[Block]= []
        self.difficulty = 5
        self.create_block(nonce=1, previous_hash="0")

    
    def get_blockchain(self) -> str:
        return [{
            "index": (block.index),
            "timestamp": block.timestamp,
            "nonce": str(block.nonce),
            "previous_hash": block.previous_hash,
            } for block in self.chain]
    # This function is created
    # to add further blocks
    # into the chain
    def create_block(self, nonce: int, previous_hash: str) -> Block:

        block = Block(len(self.chain) + 1, str(datetime.datetime.now()), nonce, previous_hash)
        self.chain.append(block)
        return block

    # This function is created
    # to display the previous block
    def print_previous_block(self) -> Block:
        return self.chain[-1]

    # This is the function for proof of work
    # and used to successfully mine the block
    def proof_of_work(self, previous_nonce: int) -> int:
        new_nonce = 1
        check_nonce = False

        while check_nonce is False:
            hash_operation = hashlib.sha256(
                str(new_nonce**2 - previous_nonce**2).encode()
            ).hexdigest()
            if hash_operation[:self.difficulty] == "00000":
                check_nonce = True
            else:
                # TODO: Change this to a random number
                new_nonce += 1

        return new_nonce

    def chain_valid(self, chain: list[Block]):
        previous_block = chain[0]

        for block in chain[1:]:
            if block.previous_hash != previous_block.hash():
                return False

            previous_nonce = previous_block.nonce
            nonce = block.nonce
            hash_operation = hashlib.sha256(
                str(nonce**2 - previous_nonce**2).encode()
            ).hexdigest()

            if hash_operation[:self.difficulty] != "00000":
                return False
            previous_block = block

        return True

    def create_fake_block(self) -> Block:
        return self.create_block(0, "0")

