import time, json, hashlib
from typing import List, Dict

class Block:
    def __init__(self, index: int, transactions: List[Dict], previous_hash: str, difficulty: int = 2):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True, default=str)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [{"action":"genesis"}], "0", self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, user: str, action: str, value: int = 1):
        self.pending_transactions.append({"user": user, "action": action, "value": value})

    def mine_block(self):
        if not self.pending_transactions:
            return None
        new_block = Block(len(self.chain), self.pending_transactions, self.chain[-1].hash, self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]
            if current.hash != current.compute_hash() or current.previous_hash != prev.hash:
                return False
        return True
