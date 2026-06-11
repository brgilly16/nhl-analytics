def rankItems(items, statsMap):
    return sorted(items, key = lambda t: t.calcPowerScore(statsMap), reverse = True)
def printRankings(items, statsMap):
    for i in range(len(items)):
        item = items[i]
        print(f"{i+1}- {item.name}: {item.calcPowerScore(statsMap):.3f}")