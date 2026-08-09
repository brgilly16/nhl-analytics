import argparse
from src.data import readAndClean, teamsFilter, playersFilter
from src.ranking import rankItems, printItems
from src.plots import plotItems
def getArgs():
    # create argumentParser
    parser = argparse.ArgumentParser()
    # add mode arg to allow users to filter between team stats and player stats or all of them
    # default set as all to select both types of stats
    parser.add_argument(
        "--mode", 
        type = str.lower,
        choices = ["teams", "players", "all"],
        default = "all")
    # add top arg to allow users to filter for how many players/teams they want to rank
    # example would be --top 15 (rank top 15 players/teams)
    # default set as None to rank all players
    parser.add_argument(
        "--top",
        type = int,
        default = None 
    )
    # add season arg to allow users to filter regular season, playoffs, or all
    # default set as all to select both seasons
    parser.add_argument(
        "--season",
        type = str.lower,
        choices = ["regular", "playoffs", "all"],
        default = "all"
    )
    # add plot arg to allow users to request a scatter plot of the rankings
    # default set as no to not plot the rankings
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
    # validate user input and set boolean for plot arg
    if top != None and top <= 0:
        print("Please enter a valid top. Top should be greater than 0.")
        return
    if plot == "yes":
        test = True
    # filter for the user requested stat and season and call the proper functions with the correct dataset
    if mode in ["teams", "all"]:
        if season in ["playoffs", "all"]:
            teamsP, model, scaler, featureNames  = teamsFilter(readAndClean("data/teams (1).csv"))
            itemsP = rankItems(teamsP, model, scaler, featureNames)
            printItems(itemsP, model, scaler, featureNames, top)
            if test:
                plotItems(itemsP, model, scaler, featureNames, top = top, title = "Playoff Teams")
        if season in ["regular", "all"]:
            teamsR, model, scaler, featureNames = teamsFilter(readAndClean("data/teams.csv"))
            itemsR = rankItems(teamsR, model, scaler, featureNames)
            printItems(itemsR, model, scaler, featureNames, top)
            if test:
                plotItems(itemsR, model, scaler, featureNames, top = top, title = "Regular Season Teams")
    if mode in ["players", "all"]:
        if season in ["playoffs", "all"]:
            playersP, model, scaler, featureNames = playersFilter(readAndClean("data/skaters.csv"))
            itemsPP = rankItems(playersP, model, scaler, featureNames)
            printItems(itemsPP, model, scaler, featureNames, top)
            if test:
                plotItems(itemsPP, model, scaler, featureNames, top = top, title = "Playoff Players")
        if season in ["regular", "all"]:
            playersR, model, scaler, featureNames = playersFilter(readAndClean("data/skaters (1).csv"))
            itemsPR = rankItems(playersR, model, scaler, featureNames)
            printItems(itemsPR, model, scaler, featureNames, top)
            if test:
                plotItems(itemsPR, model, scaler, featureNames, top = top, title = "Regular Season Players")
if __name__ == "__main__":
    main()
