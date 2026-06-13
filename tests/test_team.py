import pandas as pd
from src.stats import Stats
from src.team import Team
def testGetZ():
    df = pd.DataFrame({"XGD": [-5, -5, -5, 7]})
    stats = Stats("XGD", df)
    team = Team("test", 4, 0, 0, 0, 0)
    z = team.getZ(team.xGD, stats)
    assert z == 1