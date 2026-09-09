import os
import pandas as pd
def storeRankings(items, scores, season, category, time):
    newRankings = pd.DataFrame({
        "name": items,
        "score": scores,
        "season": [season] * len(items),
        "category": [category] * len(items),
        "time": [time] * len(items)
        })
    if not os.path.exists("data/rankings.csv"):
        newRankings.to_csv("data/rankings.csv", index=False)
        return
    df = pd.read_csv("data/rankings.csv")
    if ((df["season"] == season) & (df["category"] == category) & (df["time"] == time)).any():
        return
    df = pd.concat([df, newRankings], ignore_index=True)
    df.to_csv("data/rankings.csv", index=False)