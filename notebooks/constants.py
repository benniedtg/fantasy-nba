import os 
from dotenv import load_dotenv

load_dotenv()

DATA_DIRECTORY = os.path.join(os.getcwd().replace('notebooks', ''), 'data')

TIME_SLEEP = 3 # seconds

PLOTLY_API_KEY = os.getenv("PLOTLY_API_KEY")
PLOTLY_USERNAME = os.getenv("PLOTLY_USERNAME")

URL = "https://www.basketball-reference.com"
BOXSCORES_FORMAT = "https://www.basketball-reference.com/?month={month}&day={day}&year={year}"
SEARCH_FORMAT = "/search/search.fcgi?hint=&search={term}&pid=&idx="

URL_ROTO_FORMAT = (
    "http://rotoguru1.com/cgi-bin/hyday.pl?mon={month}&day={day}&year={year}&game=dk"
)

SEASON_DATES = {
    "2014-15": ["20141028", "20150415"],
    "2015-16": ["20151027", "20160413"],
    "2016-17": ["20161025", "20170412"],
    "2017-18": ["20171017", "20180411"],
    "2018-19": ["20181016", "20190410"],
    "2019-20": ["20191022", "20200410"],
    "2020-21": ["20201222", "20210516"],
    "2021-22": ["20211019", "20220410"],
    "2022-23": ["20221018", "20230409"],
}

DATAFRAME_VARIABLES=[
    'Name',
    'Date',
    'Team',
    # DraftKings fantasy points: FPTS = PTS + 0.5*3PTs + 1.25* TRB + 1.5AST + 2STL + 2BLK - 0.5TOV + 1.5DD + 3TD
    'FPTS',
    'Home',
    'W',
    'W_PTS',
    'L',
    'L_PTS',
    'MP',
    'FG',
    'FGA',
    'FG%',
    '3P',
    '3PA',
    '3P%',
    'FT',
    'FTA',
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "DD",
    "TD",
    "USG%",
    "DRtg",
    "ORtg",
    "AST%",
    "DRB%",
    "ORB%",
    "BLK%",
    "TOV%",
    "STL%",
    "eFG%",
]

DATAFRAME_COlUMNS = [
    "Name",
    "Date",
    "Team",
    "Home",
    "W",
    "W_PTS",
    "L",
    "L_PTS",
    "MP",
    "FG",
    "FGA",
    "FG%",
    "3P",
    "3PA",
    "3P%",
    "FT",
    "FT%",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "+-",# Net point differential when player is on court.
    "TS%", # TRUE Shooting efficiency accounting for 2P, 3P, FT.
    "eFG%",
    "3PAr",
    "FTA",
    "FTr", # Free throws per field goal attempt.
    "ORB%",
    "DRB%",
    "TRB%",#Share of available rebounds grabbed.
    "AST%",
    "STL%",
    "BLK%",
    "TOV%",
    "USG%",
    "ORtg",
    "DRtg",
    "BPM", # Overall contribution per 100 possessions.
]

DATAFRAME_FEATURES = [
    "Date",
    "Name",
    "Team",
    "Pos",
    "FPTS",
    "Salary",
    # Additional Features
    "Starter",
    "Rest",
    "Rota_All", # Rotation rank among all players on team (e.g., minutes-based).
    "Rota_Pos", #Rotation rank within position (e.g., top PG).
    "Home",
    "PG",
    "SG",
    "F",
    "C",
    "Value",
    "FPTS_std",
    # Basic Stats with weighted mean
    "PTS",
    "3P",
    "AST",
    "TRB",
    "STL",
    "BLK",
    "TOV",
    "DD",
    "TD",
    # Additional Stats with weighted mean
    "MP",
    "FT",
    "FTA",
    "FGA",
    "3PA",
    "DRB",
    "ORB",
    # Advanced Stats with weighted mean
    "USG%",
    "DRtg",
    "ORtg",
    "AST%",
    "DRB%",
    "ORB%",
    "BLK%",
    "TOV%",
    "STL%",
    "eFG%",
    "FG%",
    "3P%",
    "FT%",
]

SCORING_RULES = {
    "PTS": 1,
    "3P": 0.5,
    "TRB": 1.25,
    "AST": 1.5,
    "STL": 2,
    "BLK": 2,
    "TOV": -0.5,
}