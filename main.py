from src.data import readAndClean, teamsFilter  
def main():
    teamsP, statsMapP = teamsFilter(readAndClean("../assets/teams (1).csv"))
    teamsR, statsMapR = teamsFilter(readAndClean("../assets/teams.csv"))
    for team in teamsP:
        print(f"{team.name}: {team.calcPowerScore(statsMapP):.3f}")
    print("\n\n")
    for team in teamsR:
        print(f"{team.name}: {team.calcPowerScore(statsMapR):.3f}")
main()
