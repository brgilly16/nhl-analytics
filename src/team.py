import pandas as pd
class Team:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
    def calcPowerScore(self, model, scaler, featureNames):
        values = pd.DataFrame([self.stats])
        values = values[featureNames]
        values = scaler.transform(values)
        return model.predict(values)[0]
    def __str__(self):
        return self.name