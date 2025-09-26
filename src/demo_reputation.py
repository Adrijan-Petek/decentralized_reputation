import random
from pathlib import Path
from src.blockchain import Blockchain
from src.reputation import ReputationSystem

OUT = Path("outputs")
CHARTS = Path("charts")
OUT.mkdir(exist_ok=True)
CHARTS.mkdir(exist_ok=True)

bc = Blockchain(difficulty=2)
users = ["Alice","Bob","Charlie","Dave","Eve"]

# Simulate actions
for _ in range(10):
    for _ in range(random.randint(1,4)):
        user = random.choice(users)
        action = random.choice(["post","vote","comment"])
        value = random.randint(1,5)
        bc.add_transaction(user, action, value)
    bc.mine_block()

# Compute reputation
rep = ReputationSystem(bc)
rep.compute_scores()
rep.export_scores(OUT/"reputation.json")
rep.export_chart(CHARTS/"reputation.png")

print("Demo complete. Reputation scores exported.")
