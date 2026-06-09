import pandas as pd
class Stats:
    def __init__(self, colName, df):
        self.colName = colName
        self.df = df
    def getMu(self):
        return self.df[self.colName].mean()
    def getSd(self):
        return self.df[self.colName].std()
class Team:
    def __init__(self, name, xGD, xGP, giveawayDifferential, hdsd, aGD):
        self.name = name
        self.xGD = xGD
        self.xGP = xGP
        self.giveawayDifferential = giveawayDifferential
        self.hdsd = hdsd
        self.aGD = aGD
    def getZ(self, value, stats):
        return (value - stats.getMu()) / stats.getSd()
    def calcPowerScore(self, statsMap):
        xgdZ = self.getZ(self.xGD, statsMap["XGD"])
        xgpZ = self.getZ(self.xGP, statsMap["XGP"])
        gZ = self.getZ(self.giveawayDifferential, statsMap["GiveawayDifferential"])
        hZ = self.getZ(self.hdsd, statsMap["HDSD"])
        aZ = self.getZ(self.aGD, statsMap["AGD"])
        powerScore = 0.15 * xgdZ + 0.05 * xgpZ + 0.2 * gZ + 0.3 * hZ + 0.3 * aZ
        return powerScore
    def __str__(self):
        return self.name
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
def main():
    teamsP, statsMapP = teamsFilter(readAndClean("../assets/teams (1).csv"))
    teamsR, statsMapR = teamsFilter(readAndClean("../assets/teams.csv"))
    for team in teamsP:
        print(f"{team.name}: {team.calcPowerScore(statsMapP):.3f}")
    print()
    print()
    print()
    for team in teamsR:
        print(f"{team.name}: {team.calcPowerScore(statsMapR):.3f}")
main()
