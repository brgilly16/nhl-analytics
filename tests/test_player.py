import pandas as pd
from src.stats import Stats
from src.player import Player
def testGetZ():
    df = pd.DataFrame({"XGD": [-5, -5, -5, 7]})
    stats = Stats("XGD", df)
    player = Player("test", 0, 4, 0, 0, 0, 0) 
    z = player.getZ(player.xGD, stats)
    assert z == 1