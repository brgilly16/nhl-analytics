import pandas as pd
from src.stats import Stats
from src.team import Team
from src.player import Player
from src.downloadstandings import downloadStandings
from src.downloadgar import downloadGar
from src.calcweights import calcWeightsTeam
from src.calcweights import calcWeightsPlayer
def readAndClean(filepath):
    try:
        df = pd.read_csv(filepath)
        df = df.drop_duplicates().dropna()
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
    table = downloadStandings()
    df = df.merge(table, left_on = "team", right_on = "Team", how = "left")
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
    teamWeights = calcWeightsTeam(df)
    return teams, statsMap, teamWeights
def playersFilter(df):
    df = df[df["situation"] == "all"]
    perGameColumns = [
        "OnIce_F_goals",
        "OnIce_A_goals",
        "OnIce_F_xGoals",
        "OnIce_A_xGoals",
        "OnIce_F_shotsOnGoal",
        "OnIce_A_shotsOnGoal",
        "OnIce_F_shotAttempts",
        "OnIce_A_shotAttempts",
        "OnIce_F_unblockedShotAttempts",
        "OnIce_A_unblockedShotAttempts",
        "OnIce_F_highDangerShots",
        "OnIce_A_highDangerShots",
        "I_F_goals",
        "I_F_primaryAssists",
        "I_F_secondaryAssists",
        "I_F_points",
        "I_F_shotsOnGoal",
        "I_F_shotAttempts",
        "I_F_unblockedShotAttempts",
        "I_F_missedShots",
        "I_F_blockedShotAttempts",
        "I_F_takeaways",
        "I_F_giveaways",
        "I_F_hits",
        "I_F_rebounds",
        "I_F_reboundGoals",
        "I_F_savedShotsOnGoal"
    ]
    for column in perGameColumns:
        if column in df.columns:
            df[column] = df[column] / df["games_played"]
    model, scaler, featureNames = calcWeightsPlayer()
    players = []
    for i in range(len(df)):
        row = df.iloc[i]
        playerName = row["name"]
        stats = {}
        for feature in featureNames:
            stats[feature] = row[feature]
        players.append(Player(playerName, stats))
    return players, model, scaler, featureNames