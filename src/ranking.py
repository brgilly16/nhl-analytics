def rankItems(items, model, scaler, featureNames):
    return sorted(items, key = lambda t: t.calcPowerScore(model, scaler, featureNames), reverse = True)
def printItems(items, model, scaler, featureNames, top = None):
    if top != None:
        items = items[0:top]
    for i in range(len(items)):
        item = items[i]
        print(f"{i+1}. {item.name}: {item.calcPowerScore(model, scaler, featureNames):.3f}")