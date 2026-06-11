import argparse
from src.data import readAndClean, teamsFilter, playersFilter
from src.ranking import printRankings, rankItems  
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", 
        type = str.lower,
        choices = ["teams", "players", "all"],
        default = "all")
    parser.add_argument(
        "--top",
        type = int,
        default = None 
    )
    parser.add_argument(
        "--season",
        type = str.lower,
        choices = ["regular", "playoffs", "all"],
        default = "all"
    )
    return parser.parse_args()
def main():
    args = getArgs()
    mode = args.mode
    top = args.top
    season = args.season
    if mode in ["teams", "all"]:
        if season in ["playoffs", "all"]:
            teamsP, statsMapP = teamsFilter(readAndClean("data/teams (1).csv"))
            printRankings(rankItems(teamsP, statsMapP), statsMapP, top)
        if season in ["regular", "all"]:
            teamsR, statsMapR = teamsFilter(readAndClean("data/teams.csv"))
            printRankings(rankItems(teamsR, statsMapR), statsMapR, top)
    if mode in ["players", "all"]:
        if season in ["playoffs", "all"]:
            playersR, statsMapPlayers = playersFilter(readAndClean("data/skaters.csv"))
            printRankings(rankItems(playersR, statsMapPlayers), statsMapPlayers, top)
        if season in ["regular", "all"]:
            playersP, statsMapPlayoffPlayers = playersFilter(readAndClean("data/skaters (1).csv"))
            printRankings(rankItems(playersP, statsMapPlayoffPlayers), statsMapPlayoffPlayers, top)
if __name__ == "__main__":
    main()
