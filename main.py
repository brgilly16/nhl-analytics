import argparse
from src.data import readAndClean, teamsFilter, playersFilter
from src.ranking import printRankings, rankItems  
from src.plots import plotRankings
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
    parser.add_argument(
        "--plot",
        type = str.lower,
        choices = ["yes","no"],
        default = "yes"
    )
    return parser.parse_args()
def main():
    args = getArgs()
    mode = args.mode
    top = args.top
    season = args.season
    plot = args.plot
    test = False
    if plot == "yes":
        test = True
    if mode in ["teams", "all"]:
        if season in ["playoffs", "all"]:
            teamsP, statsMapP = teamsFilter(readAndClean("data/teams (1).csv"))
            itemsP = rankItems(teamsP, statsMapP)
            printRankings(itemsP, statsMapP, top)
            if test:
                plotRankings(itemsP, statsMapP, top = top, title = "Playoff Teams")
        if season in ["regular", "all"]:
            teamsR, statsMapR = teamsFilter(readAndClean("data/teams.csv"))
            itemsR = rankItems(teamsR, statsMapR)
            printRankings(itemsR, statsMapR, top)
            if test:
                plotRankings(itemsR, statsMapR, top = top, title = "Regular Season Teams")
    if mode in ["players", "all"]:
        if season in ["playoffs", "all"]:
            playersP, statsMapPlayoffPlayers = playersFilter(readAndClean("data/skaters.csv"))
            itemsPP = rankItems(playersP, statsMapPlayoffPlayers)
            printRankings(itemsPP, statsMapPlayoffPlayers, top)
            if test:
                plotRankings(itemsPP, statsMapPlayoffPlayers, top = top, title = "Playoff Players")
        if season in ["regular", "all"]:
            playersR, statsMapPlayers = playersFilter(readAndClean("data/skaters (1).csv"))
            itemsPR = rankItems(playersR, statsMapPlayers)
            printRankings(itemsPR, statsMapPlayers, top)
            if test:
                plotRankings(itemsPR, statsMapPlayers, top = top, title = "Regular Season Players")
if __name__ == "__main__":
    main()
