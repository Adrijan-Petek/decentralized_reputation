from src.blockchain import Blockchain
from src.reputation import ReputationSystem

def test_reputation_scores():
    bc = Blockchain()
    bc.add_transaction("Alice", "post", 3)
    bc.add_transaction("Bob", "vote", 2)
    bc.mine_block()
    
    rep = ReputationSystem(bc)
    scores = rep.compute_scores()
    assert scores["Alice"] == 3
    assert scores["Bob"] == 2
