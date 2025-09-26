import pytest
from src.blockchain import Blockchain

def test_genesis_block():
    bc = Blockchain()
    assert len(bc.chain) == 1
    assert bc.chain[0].transactions[0]["action"] == "genesis"

def test_add_transaction_and_mine():
    bc = Blockchain()
    bc.add_transaction("Alice", "post", 5)
    block = bc.mine_block()
    assert block.transactions[0]["user"] == "Alice"
    assert bc.is_chain_valid()
