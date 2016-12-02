import InformationParser
import os.path


DB_NAME = "database.sqlite"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.sqlite")
team_parse = InformationParser.Team_Dao(db_path)
print team_parse.get_team_by_fullname("KRC Genk").api_id
match_parse = InformationParser.Match_Dao(db_path)
print match_parse.get_match_by_teams_season(9987, 9993, "2008/2009").away_Team_goal
print team_parse.get_team_by_id(team_parse.get_team_by_fullname("Arsenal").api_id).team_fifa_id
ms = match_parse.get_last5_matches_of_team(team_parse.get_team_by_id(team_parse.get_team_by_fullname("Arsenal").api_id),
                                      "2015-10-01")


def research_matches(matches):

    for i in matches:
        print i.get_result(), team_parse.get_team_by_id(i.away_Team).team_name, i.date

research_matches(ms)
