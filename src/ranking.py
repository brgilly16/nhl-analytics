def rankItems(items, statsMap, weights):
    return sorted(items, key = lambda t: t.calcPowerScore(statsMap, weights), reverse = True)
def printRankings(items, statsMap, weights, top = None):
    if top != None:
        items = items[0:top]
    for i in range(len(items)):
        item = items[i]
        print(f"{i+1}. {item.name}: {item.calcPowerScore(statsMap, weights):.3f}")