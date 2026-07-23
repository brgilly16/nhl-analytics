import pandas as pd
from src.downloadgar import downloadGar
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.metrics import r2_score
def calcWeightsTeam(df):
    X = df[["XGD", "xGoalsPercentage", "GiveawayDifferential", "HDSD", "AGD"]]
    Y = df["PTS%"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    modelOne = LinearRegression()
    modelTwo = RidgeCV(alphas=[0.001, 0.01, 0.1, 1, 10, 100])
    modelOne.fit(X_train_scaled, Y_train)
    modelTwo.fit(X_train_scaled, Y_train)
    predictionsOne = modelOne.predict(X_test_scaled)
    predictionsTwo = modelTwo.predict(X_test_scaled)
    accOne = r2_score(Y_test, predictionsOne)
    accTwo = r2_score(Y_test, predictionsTwo)
    if accOne > accTwo:
        weights = {"XGD": modelOne.coef_[0],
                   "XGP": modelOne.coef_[1],
                   "GiveawayDifferential": modelOne.coef_[2],
                    "HDSD": modelOne.coef_[3],
                    "AGD": modelOne.coef_[4]
        }
        print("modelOne chosen")
    else:
        weights = {"XGD": modelTwo.coef_[0],
                   "XGP": modelTwo.coef_[1],
                   "GiveawayDifferential": modelTwo.coef_[2],
                    "HDSD": modelTwo.coef_[3],
                    "AGD": modelTwo.coef_[4]
        }
        print("modelTwo chosen")
    print(weights)
    print(accOne, accTwo)
    return weights
def calcWeightsPlayer():
    df = pd.read_csv("data/skaters (1).csv")
    df = df.drop_duplicates().dropna()
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
    table = downloadGar()
    df = df.merge(table, left_on = ["season", "name"], right_on = ["Season","Player"], how = "left")
    df = df.dropna(subset=["GAR"])
    df = df[df["games_played"] > 20]
    exclude = [
    "GAR",
    "WAR",
    "SPAR",
    "EVO_GAR",
    "EVD_GAR",
    "PPO_GAR",
    "SHD_GAR",
    "Take_GAR",
    "Draw_GAR",
    "Off_GAR",
    "Def_GAR",
    "Pens_GAR",
    "playerId",
    "name",
    "Player",
    "team",
    "Team",
    "season",
    "Season",
    "position",
    "Position",
    "situation",
    "GP",
    "TOI_All",
    "I_F_shifts",
    "faceoffsWon",
    "penalityMinutes",
    "gameScore",
    "xGoalsForAfterShifts",
    "xGoalsAgainstAfterShifts",
    "corsiForAfterShifts",
    "corsiAgainstAfterShifts",
    "fenwickForAfterShifts",
    "fenwickAgainstAfterShifts"
    ]
    X = df.drop(columns=exclude)
    X = X.select_dtypes(include="number")    
    Y = df["GAR"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    modelOne = LinearRegression()
    modelTwo = RidgeCV(alphas=[0.001, 0.01, 0.1, 1, 10, 100])
    modelThree = LassoCV(alphas=[0.001, 0.01, 0.1, 1, 10], cv=5, max_iter=1000000, random_state=42)
    modelOne.fit(X_train_scaled, Y_train)
    modelTwo.fit(X_train_scaled, Y_train)
    modelThree.fit(X_train_scaled, Y_train)
    predictionsOne = modelOne.predict(X_test_scaled)
    predictionsTwo = modelTwo.predict(X_test_scaled)
    predictionsThree = modelThree.predict(X_test_scaled)
    accOne = r2_score(Y_test, predictionsOne)
    accTwo = r2_score(Y_test, predictionsTwo)
    accThree = r2_score(Y_test, predictionsThree)
    if accOne >= accTwo and accOne >= accThree:
        bestModel = modelOne
        print("modelOne chosen")
    elif accTwo >= accOne and accTwo >= accThree:
        bestModel = modelTwo
        print("modelTwo chosen")
    else:
        bestModel = modelThree
        print("modelThree chosen")
    print(accOne, accTwo, accThree)
    featureNames = X.columns.tolist()
    return bestModel, scaler, featureNames