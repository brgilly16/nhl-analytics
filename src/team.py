class Team:
    def __init__(self, name, xGD, xGP, giveawayDifferential, hdsd, aGD):
        self.name = name
        self.xGD = xGD
        self.xGP = xGP
        self.giveawayDifferential = giveawayDifferential
        self.hdsd = hdsd
        self.aGD = aGD
    def getZ(self, value, stats):
        return (value - stats.getMu()) / stats.getSd()
    def calcPowerScore(self, statsMap):
        xgdZ = self.getZ(self.xGD, statsMap["XGD"])
        xgpZ = self.getZ(self.xGP, statsMap["XGP"])
        gZ = self.getZ(self.giveawayDifferential, statsMap["GiveawayDifferential"])
        hZ = self.getZ(self.hdsd, statsMap["HDSD"])
        aZ = self.getZ(self.aGD, statsMap["AGD"])
        powerScore = 0.15 * xgdZ + 0.05 * xgpZ + 0.2 * gZ + 0.3 * hZ + 0.3 * aZ
        return powerScore
    def __str__(self):
        return self.name