import json
import pandas as pd
from src.blockchain import Blockchain

class ReputationSystem:
    def __init__(self, blockchain: Blockchain):
        self.bc = blockchain
        self.scores = {}

    def compute_scores(self):
        self.scores = {}
        for block in self.bc.chain:
            for tx in block.transactions:
                if "user" not in tx:  # skip genesis block
                    continue
                user = tx["user"]
                value = tx.get("value", 1)
                self.scores[user] = self.scores.get(user, 0) + value
        return self.scores

    def export_scores(self, path="outputs/reputation.json"):
        with open(path, "w") as f:
            json.dump(self.scores, f, indent=2)

    def export_chart(self, path="charts/reputation.png"):
        import matplotlib.pyplot as plt
        df = pd.DataFrame(list(self.scores.items()), columns=["User", "Score"]).sort_values("Score", ascending=False)
        plt.figure(figsize=(10, 6))
        plt.bar(df["User"], df["Score"], color="skyblue")
        plt.xticks(rotation=45, ha="right")
        plt.title("User Reputation Scores")
        plt.tight_layout()
        plt.savefig(path)
        plt.close()
