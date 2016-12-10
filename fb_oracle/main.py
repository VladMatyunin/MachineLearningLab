import InformationParser
import os.path
import math
import Neuron

input_parameters = ["LAST_5_GAMES", "HISTORY", "PLAYERS"]

DB_NAME = "database.sqlite"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.sqlite")
team_parse = InformationParser.Team_Dao(db_path)
# print team_parse.get_team_by_fullname("Arsenal").api_id
match_parse = InformationParser.Match_Dao(db_path)


# Returns the array of team result, 1-win, 0-draw, -1-lose
# gets the array of matches to research and the team to consider
def research_matches(matches, team_id):
    result = []
    for i in matches:
        result.append(i.get_team_result(team_id))
    return result


# converts the array of 1, 0 or -1 to a number
# like an average
def convert(array):
    sum = 0
    for i in array:
        sum += i
    return float(sum) / len(array)

# print research_matches(ms, team_parse.get_team_by_fullname("Arsenal").api_id)
# print convert(research_matches(ms, team_parse.get_team_by_fullname("Arsenal").api_id))

# print match_parse.get_players_func(1218864)
# print research_matches(ms, 9825)
# print convert(match_parse.get_statistics(team_parse.get_team_by_fullname("Arsenal").api_id,
#                                   team_parse.get_team_by_fullname("Manchester United").api_id))
# my_neural_net = Neuron.NeuronNet(3, ["x", "y", "z"], 3, "function")
#
#
# def test_function(x):
#     e = math.e
#     for i in x:
#         print math.tan((math.exp(2*i)-1)/(math.exp(2*i)+1))
# x = [1, 2, 3]
# test_function(x)
team1_id = team_parse.get_team_by_fullname("Arsenal").api_id
team2_id = team_parse.get_team_by_fullname("Manchester United").api_id
history = convert(match_parse.get_statistics(team1_id, team2_id))
last_team1_match = match_parse.get_last5_matches_of_team(team_parse.get_team_by_id(team1_id), "2014-10-01")
last_team2_match = match_parse.get_last5_matches_of_team(team_parse.get_team_by_id(team2_id), "2014-10-01")
k1 = convert(research_matches(last_team1_match, team1_id))
k2 = convert(research_matches(last_team2_match, team2_id))
k1 = float(k1)
total_k = k1/k2
# TODO: get match_id between Arsenal and MU
k3 = 0.7
neuron_net = Neuron.NeuronNet(3, input_parameters, 3)
# print (neuron_net.get_input_parameters())
# print (neuron_net.get_from_input_to_hidden_ways())
a = [history,total_k,k3]
neuron_net.execute(a)

