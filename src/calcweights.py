import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def calcWeightsTeam(df):
    X = df[["XGD", "XGP", "GiveawayDifferential", "HDSD", "AGD"]]
    Y = df[""]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    modelOne = LinearRegression()
    modelTwo = Ridge(alpha=1.0)
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
    else:
        weights = {"XGD": modelTwo.coef_[0],
                   "XGP": modelTwo.coef_[1],
                   "GiveawayDifferential": modelTwo.coef_[2],
                    "HDSD": modelTwo.coef_[3],
                    "AGD": modelTwo.coef_[4]
        }
    return weights
def calcWeightsPlayer(df):
    X = df[["XGD", "XGP", "PPG", "GD", "HDSD", "AGD"]]
    Y = df[""]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    modelOne = LinearRegression()
    modelTwo = Ridge(alpha=1.0)
    modelOne.fit(X_train_scaled, Y_train)
    modelTwo.fit(X_train_scaled, Y_train)
    predictionsOne = modelOne.predict(X_test_scaled)
    predictionsTwo = modelTwo.predict(X_test_scaled)
    accOne = r2_score(Y_test, predictionsOne)
    accTwo = r2_score(Y_test, predictionsTwo)
    if accOne > accTwo:
        weights = {"XGD": modelOne.coef_[0],
                   "XGP": modelOne.coef_[1],
                   "PPG": modelOne.coef_[2],
                   "GD": modelOne.coef_[3],
                    "HDSD": modelOne.coef_[4],
                    "AGD": modelOne.coef_[5]
        }
    else:
        weights = {"XGD": modelTwo.coef_[0],
                   "XGP": modelTwo.coef_[1],
                   "PPG": modelTwo.coef_[2],
                   "GiveawayDifferential": modelTwo.coef_[3],
                    "HDSD": modelTwo.coef_[4],
                    "AGD": modelTwo.coef_[5]
        }
    return weights