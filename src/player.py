class Player:
    def __init__(self, name, xGPD, xGD, pPG, giveawayDifferential, hdsd, aGD):
        self.name = name
        self.xGD = xGD
        self.xGPD = xGPD
        self.pPG = pPG
        self.giveawayDifferential = giveawayDifferential
        self.hdsd = hdsd
        self.aGD = aGD
    def getZ(self, value, stats):
        return (value - stats.getMu()) / stats.getSd()
    def calcPowerScore(self, statsMap):
        xgdZ = self.getZ(self.xGD, statsMap["XGD"])
        xgpZ = self.getZ(self.xGPD, statsMap["XGP"])
        pZ = self.getZ(self.pPG, statsMap["PPG"])
        gZ = self.getZ(self.giveawayDifferential, statsMap["GD"])
        hZ = self.getZ(self.hdsd, statsMap["HDSD"])
        aZ = self.getZ(self.aGD, statsMap["AGD"])
        powerScore = 0.2 * xgdZ + 0.1 * xgpZ + 0.1 * pZ + 0.2 * gZ + 0.2 * hZ + 0.2 * aZ
        return powerScore
    def __str__(self):
        return self.name