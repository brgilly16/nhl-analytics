class Stats:
    def __init__(self, colName, df):
        self.colName = colName
        self.df = df
    def getMu(self):
        return self.df[self.colName].mean()
    def getSd(self):
        return self.df[self.colName].std()