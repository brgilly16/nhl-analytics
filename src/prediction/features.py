import pandas as pd
from sklearn.linear_model import LinearRegression
# Features will eventually include: Team PowerScore, Team Injury representation, Team Goaltending, HomeIce
# Target will be Team Goals For.
def getFeatures(team, season, time):
    df = pd.read_csv("data/rankings.csv")
    df = df[(df["season"] == season) & (df["time"] == time) & (df["name"] == team)]
    teamScore = df["score"]
    