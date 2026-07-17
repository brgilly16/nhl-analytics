import pandas as pd
def downloadStandings():
    tables = pd.read_html("https://www.hockey-reference.com/leagues/NHL_2026_standings.html")
    tableOne = tables[0]
    tableTwo = tables[1] #hockey reference includes multiple different tables. we want indecies zero and one.
    tableOne = pd.concat([tableOne,tableTwo], ignore_index=True)
    tableOne = tableOne.rename(columns={"Unnamed: 0": "Team"}) # rename team column to more understandable name
    tableOne = tableOne[["Team", "PTS%"]]
    tableOne = tableOne[tableOne["Team"].str.contains("Division") == False] #remove headers
    tableOne["Team"] = tableOne["Team"].str.replace("*", "")
    teamMap = {
    "Anaheim Ducks": "ANA",
    "Boston Bruins": "BOS",
    "Buffalo Sabres": "BUF",
    "Calgary Flames": "CGY",
    "Carolina Hurricanes": "CAR",
    "Chicago Blackhawks": "CHI",
    "Colorado Avalanche": "COL",
    "Columbus Blue Jackets": "CBJ",
    "Dallas Stars": "DAL",
    "Detroit Red Wings": "DET",
    "Edmonton Oilers": "EDM",
    "Florida Panthers": "FLA",
    "Los Angeles Kings": "LAK",
    "Minnesota Wild": "MIN",
    "Montreal Canadiens": "MTL",
    "Nashville Predators": "NSH",
    "New Jersey Devils": "NJD",
    "New York Islanders": "NYI",
    "New York Rangers": "NYR",
    "Ottawa Senators": "OTT",
    "Philadelphia Flyers": "PHI",
    "Pittsburgh Penguins": "PIT",
    "San Jose Sharks": "SJS",
    "Seattle Kraken": "SEA",
    "St. Louis Blues": "STL",
    "Tampa Bay Lightning": "TBL",
    "Toronto Maple Leafs": "TOR",
    "Utah Mammoth": "UTA", 
    "Vancouver Canucks": "VAN",
    "Vegas Golden Knights": "VGK",
    "Washington Capitals": "WSH",
    "Winnipeg Jets": "WPG"
    }
    tableOne["Team"] = tableOne["Team"].map(teamMap)
    return tableOne