from blockchain.Blockchain import Blockchain

class Node:
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain

    def mine_block(self):
        previous_block = self.blockchain.print_previous_block()
        previous_nonce = previous_block.nonce
        nonce = self.blockchain.proof_of_work(previous_nonce)
        return nonce
