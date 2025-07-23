
import hashlib
import time

class Block:
    def __init__(self, block_id, timestamp, data, previous_hash, nonce=0):
        # Initialize block properties
        self.block_id = block_id
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.nonce = nonce  
        self.hash = self.compute_hash()  # Calculate the block's hash upon creation

    def compute_hash(self):
        # Concatenate block properties and return their SHA-256 hash
        block_string = f"{self.block_id}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (f"Block ID: {self.block_id}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Nonce: {self.nonce}\n"
                f"Hash: {self.hash}")

def create_blockchain(num_blocks=3):
    blockchain = []
    # Create the genesis block (first block, has no predecessor)
    genesis_block = Block(
        block_id=0,
        timestamp=time.time(),
        data="Genesis Block",
        previous_hash="0"  # No previous hash for genesis block
    )
    blockchain.append(genesis_block)
    
    # Create subsequent blocks
    for i in range(1, num_blocks):
        time.sleep(1)  # Ensure different timestamps for each block
        new_block = Block(
            block_id=i,
            timestamp=time.time(),
            data=f"Transaction {i}",
            previous_hash=blockchain[-1].hash  # Link to previous block's hash
        )
        blockchain.append(new_block)
    
    return blockchain

# Test the blockchain creation and print each block
blockchain = create_blockchain()
for block in blockchain:
    print(block)
    print("-" * 50)
