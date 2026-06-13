import pandas as pd
from src.stats import Stats
def testGetMu():
    df = pd.DataFrame({"XGD": [-100, 5, 50, 200, 1000, 1545]})
    stats = Stats("XGD", df)
    assert stats.getMu() == 450
def testGetSD():
    df = pd.DataFrame({"XGF": [1, 1, 1, 5]})
    stats = Stats("XGF", df)
    assert stats.getSd() == 2