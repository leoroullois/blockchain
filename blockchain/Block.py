import hashlib
import json

class Block:
    def __init__(self, index: int, timestamp: str, nonce: int, previous_hash: str, data: str):
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data

    def get_block(self) -> dict:
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "previous_hash": self.previous_hash,
            "data": self.data
        }

    def hash(self) -> str:
        encoded_block = json.dumps(self.get_block(), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
