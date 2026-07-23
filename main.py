import argparse
from src.data import readAndClean, teamsFilter, playersFilter
from src.ranking import printPlayers, rankPlayers, rankItems, printRankings
from src.plots import plotRankings, plotPlayers
from src.calcweights import calcWeightsTeam, calcWeightsPlayer
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
        choices = ["yes", "no"],
        default = "no"
    )
    return parser.parse_args()
def main():
    args = getArgs()
    mode = args.mode
    top = args.top
    season = args.season
    plot = args.plot
    test = False
    weights = []
    if top != None and top <= 0:
        print("Please enter a valid top. Top should be greater than 0.")
        return
    if plot == "yes":
        test = True
    if mode in ["teams", "all"]:
        if season in ["playoffs", "all"]:
            teamsP, statsMapP, weights  = teamsFilter(readAndClean("data/teams (1).csv"))
            itemsP = rankItems(teamsP, statsMapP, weights)
            printRankings(itemsP, statsMapP, weights, top)
            if test:
                plotRankings(itemsP, statsMapP, weights, top = top, title = "Playoff Teams")
        if season in ["regular", "all"]:
            teamsR, statsMapR, weights = teamsFilter(readAndClean("data/teams.csv"))
            itemsR = rankItems(teamsR, statsMapR, weights)
            printRankings(itemsR, statsMapR, weights, top)
            if test:
                plotRankings(itemsR, statsMapR, weights, top = top, title = "Regular Season Teams")
    if mode in ["players", "all"]:
        if season in ["playoffs", "all"]:
            playersP, model, scaler, featureNames = playersFilter(readAndClean("data/skaters.csv"))
            itemsPP = rankPlayers(playersP, model, scaler, featureNames)
            printPlayers(itemsPP, model, scaler, featureNames, top)
            if test:
                plotPlayers(itemsPP, model, scaler, featureNames, top = top, title = "Playoff Players")
        if season in ["regular", "all"]:
            playersR, model, scaler, featureNames = playersFilter(readAndClean("data/skaters (1).csv"))
            itemsPR = rankPlayers(playersR, model, scaler, featureNames)
            printPlayers(itemsPR, model, scaler, featureNames, top)
            if test:
                plotPlayers(itemsPR, model, scaler, featureNames, top = top, title = "Regular Season Players")
if __name__ == "__main__":
    main()
