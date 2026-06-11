from src.data import readAndClean, teamsFilter, playersFilter
from src.ranking import printRankings, rankItems  
def main():
    teamsP, statsMapP = teamsFilter(readAndClean("data/teams (1).csv"))
    printRankings(rankItems(teamsP, statsMapP), statsMapP)
    teamsR, statsMapR = teamsFilter(readAndClean("data/teams.csv"))
    printRankings(rankItems(teamsR, statsMapR), statsMapR)
    playersR, statsMapPlayers = playersFilter(readAndClean("data/skaters.csv"))
    printRankings(rankItems(playersR, statsMapPlayers), statsMapPlayers)
    playersP, statsMapPlayoffPlayers = playersFilter(readAndClean("data/skaters (1).csv"))
    printRankings(rankItems(playersP, statsMapPlayoffPlayers), statsMapPlayoffPlayers)
if __name__ == "__main__":
    main()
