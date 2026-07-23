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
    df["XGP"] = df["onIce_xGoalsPercentage"] / df["games_played"] - df["offIce_xGoalsPercentage"] / df["games_played"]
    df["XGD"] = df["OnIce_F_xGoals"] / df["games_played"] - df["OnIce_A_xGoals"] / df["games_played"]
    df["PPG"] = df["I_F_points"] / df["games_played"]
    df["GD"] = df["I_F_takeaways"] / df["games_played"] - df["I_F_giveaways"] / df["games_played"]
    df["HDSD"] = df["OnIce_F_highDangerShots"] / df["games_played"] - df["OnIce_A_highDangerShots"] / df["games_played"]
    df["AGD"] = df["OnIce_F_goals"] / df["games_played"] -df["OnIce_A_goals"] / df["games_played"]
    statsMap = {
        "XGP": Stats("XGP", df),
        "XGD": Stats("XGD", df),
        "PPG": Stats("PPG", df),
        "GD": Stats("GD", df),
        "HDSD": Stats("HDSD", df),
        "AGD": Stats("AGD", df)
    }
    table = downloadGar()
    df = df.merge(table, left_on = ["season", "name"], right_on = ["Season","Player"], how = "left")
    df = df.dropna(subset=["GAR"])
    df = df[df["games_played"] > 20]
    print(df.columns.tolist())
    playerWeights = calcWeightsPlayer(df)
    players = []
    for i in range(len(df)):
        playerName = df.iloc[i]["name"]
        xGP = df.iloc[i]["XGP"]
        xGD = df.iloc[i]["XGD"]
        pPG = df.iloc[i]["PPG"]
        gD = df.iloc[i]["GD"]
        hDSD = df.iloc[i]["HDSD"]
        aGD = df.iloc[i]["AGD"]
        players.append(Player(playerName, xGP, xGD, pPG, gD, hDSD, aGD))
    return players, statsMap, playerWeights