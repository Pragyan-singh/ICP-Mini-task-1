import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block #{self.index}\nData: {self.data}\nHash: {self.hash}\nPrev Hash: {self.previous_hash}\n"

# Create a simple blockchain
blockchain = [Block(0, time.time(), "Genesis Block", "0")]
for i in range(1, 3):
    blockchain.append(Block(i, time.time(), f"Block {i} Data", blockchain[i-1].hash))

# Print blocks
for block in blockchain:
    print(block)

# Tamper with Block 1
print("\n--- Tampering with Block 1 ---")
blockchain[1].data = "Hacked Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Show new state
for block in blockchain:
    print(block)
