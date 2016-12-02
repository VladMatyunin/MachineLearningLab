class Team:
    api_id = 0
    team_name = ""
    team_fifa_id = 0

    def __init__(self, api_id, name, fifa_id):
        self.team_name = name
        self.api_id = api_id
        self.team_fifa_id = fifa_id


class Match:
    away_Team = Team
    home_Team = Team
    season = ""
    date = ""
    home_Team_goal = 0
    away_Team_goal = 0

    def __init__(self, home_team, away_team, season, h_t_goal, a_t_goal, date):
        self.away_Team = away_team
        self.home_Team = home_team
        self.season = season
        self.home_Team_goal = h_t_goal
        self.away_Team_goal = a_t_goal
        self.date = date

    def get_result(self):
        if self.home_Team_goal > self.away_Team_goal: return 1
        if self.home_Team_goal == self.away_Team_goal: return 0
        return -1
