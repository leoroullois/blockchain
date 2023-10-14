from blockchain.Block import Block
import random

class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.difficulty = 4
        self.create_block(
            nonce=1, previous_hash="0", data="genesis_block", timestamp="0"
        )

    def get_blockchain(self) -> str:
        return [
            {
                "index": (block.index),
                "timestamp": block.timestamp,
                "nonce": str(block.nonce),
                "previous_hash": block.previous_hash,
                "hash": block.hash(),
                "data": block.data,
            }
            for block in self.chain
        ]

    def create_block(
        self, nonce: int, previous_hash: str, data: str, timestamp: str
    ) -> Block:
        block = Block(
            len(self.chain) + 1,
            timestamp,
            nonce,
            previous_hash,
            data,
        )
        self.chain.append(block)
        return block

    def print_previous_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, previous_hash: str, data: str, timestamp: str) -> int:
        new_nonce = 1
        check_nonce = False

        while check_nonce is False:
            block = Block(
                index=len(self.chain) + 1,
                timestamp=timestamp,
                nonce=new_nonce,
                previous_hash=previous_hash,
                data=data,
            )
            if block.hash()[: self.difficulty] == "0" * self.difficulty:
                check_nonce = True
            else:
                new_nonce = random.randint(1, 2**32)

        return new_nonce

    def chain_valid(self, chain: list[Block]):
        previous_block = chain[0]

        for block in chain[1:]:
            if block.previous_hash != previous_block.hash():
                return False

            if block.hash()[: self.difficulty] != "0" * self.difficulty:
                return False
            previous_block = block

        return True

    def create_fake_block(self) -> Block:
        return self.create_block(
            nonce=0, previous_hash="0", data="fake_data", timestamp="0"
        )
