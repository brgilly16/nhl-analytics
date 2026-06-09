import pandas as pd
from src.stats import Stats
from src.team import Team
def readAndClean(filepath):
    try:
        df = pd.read_csv(filepath)
        df = df.drop_duplicates().dropna()
        print("File read and cleaned successfully!")
        return df
    except FileNotFoundError:
        print("File is not found!")
        return
def teamsFilter(df):
    df = df[df["situation"] == "all"]
    df["XGD"] = df["xGoalsFor"] / df["games_played"] - df["xGoalsAgainst"] / df["games_played"]
    df["GiveawayDifferential"] = df["giveawaysAgainst"] / df["games_played"] - df["giveawaysFor"] / df["games_played"]
    df["HDSD"] = df["highDangerShotsFor"] / df["games_played"] - df["highDangerShotsAgainst"] / df["games_played"]
    df["AGD"] = df["goalsFor"] / df["games_played"] - df["goalsAgainst"] / df["games_played"]
    statsMap = {
        "XGD": Stats("XGD", df),
        "GiveawayDifferential": Stats("GiveawayDifferential", df),
        "HDSD": Stats("HDSD", df),
        "XGP": Stats("xGoalsPercentage", df),
        "AGD": Stats("AGD", df)
    }
    teams = []
    for i in range(len(df)):
        teamName = df.iloc[i]["team"]
        xGD = df.iloc[i]["XGD"]
        xGP = df.iloc[i]["xGoalsPercentage"]
        giveawayDifferential = df.iloc[i]["GiveawayDifferential"]
        hdsd = df.iloc[i]["HDSD"]
        aGD = df.iloc[i]["AGD"]
        teams.append(Team(teamName, xGD, xGP, giveawayDifferential, hdsd, aGD))  
    teams.sort(key=lambda t: t.calcPowerScore(statsMap), reverse=True)
    return teams, statsMap   