from src.data import readAndClean, teamsFilter, playersFilter  
def main():
    teamsP, statsMapP = teamsFilter(readAndClean("data/teams (1).csv"))
    teamsR, statsMapR = teamsFilter(readAndClean("data/teams.csv"))
    playersR, statsMapPlayers = playersFilter(readAndClean("data/skaters.csv"))
    playersP, statsMapPlayoffPlayers =  playersFilter(readAndClean("data/skaters (1).csv"))
    for team in teamsP:
        print(f"{team.name}: {team.calcPowerScore(statsMapP):.3f}")
    print("\n\n")
    for team in teamsR:
        print(f"{team.name}: {team.calcPowerScore(statsMapR):.3f}")
    for player in playersR:
        print(f"{player.name}: {player.calcPowerScore(statsMapPlayers):.3f}")
    for player in playersP:
        print(f"{player.name}: {player.calcPowerScore(statsMapPlayoffPlayers):.3f}")
if __name__ == "__main__":
    main()
