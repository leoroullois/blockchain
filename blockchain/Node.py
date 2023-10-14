from blockchain.Blockchain import Blockchain

class Node:
    def __init__(self, blockchain: Blockchain, i: int):
        self.blockchain = blockchain
        self.id = i

    def mine_block(self, data: str, timestamp: str):
        previous_block = self.blockchain.print_previous_block()
        nonce = self.blockchain.proof_of_work(
            previous_hash=previous_block.hash(),
            data=data,
            timestamp=timestamp,
        )
        return nonce
