import InformationParser
import os.path

DB_NAME = "database.sqlite"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.sqlite")
team_parse = InformationParser.Team_Dao(db_path)
# print team_parse.get_team_by_fullname("Arsenal").api_id
match_parse = InformationParser.Match_Dao(db_path)
ms = match_parse.get_last5_matches_of_team(team_parse.get_team_by_id(team_parse.get_team_by_fullname("Arsenal").api_id),
                                           "2014-10-01")


# Returns the array of team result, 1-win, 0-draw, -1-lose
def research_matches(matches, team_id):
    result = []
    for i in matches:
        result.append(i.get_team_result(team_id))
    return result

# print match_parse.get_players_func(1218864)
# print research_matches(ms, 9825)
print match_parse.get_statistics(team_parse.get_team_by_fullname("Arsenal").api_id,
                                  team_parse.get_team_by_fullname("Manchester United").api_id)
