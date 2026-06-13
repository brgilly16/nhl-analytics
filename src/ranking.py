def rankItems(items, statsMap):
    return sorted(items, key = lambda t: t.calcPowerScore(statsMap), reverse = True)
def printRankings(items, statsMap, top):
    if top != None:
        items = items[0:top]
    else:
        print("Please enter a valid top. Top should be greater than 0.")
        return
    for i in range(len(items)):
        item = items[i]
        print(f"{i+1}. {item.name}: {item.calcPowerScore(statsMap):.3f}")