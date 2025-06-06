import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = ""

    def calculate_hash(self):
        content = f"{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        start = time.time()
        attempts = 0

        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
            attempts += 1

        end = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end - start:.4f} seconds")

block = Block("Mining Simulation Data")
block.mine_block(difficulty=4)
