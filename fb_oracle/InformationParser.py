from __future__ import division
import sqlite3
import os.path
import Entity


class Team_Dao:
    def __init__(self, db_path="database.sqlite"):
        db_connection = sqlite3.connect(db_path)
        self.cursor = db_connection.cursor()

    def get_team_by_id(self, team_id):
        row = self.cursor.execute("SELECT * FROM Team WHERE team_api_id =?", (team_id,)).fetchall()[0]
        team = Entity.Team(row[1], row[3], row[2])
        return team

    def get_team_by_fullname(self, fullname):
        row = self.cursor.execute("SELECT * FROM Team WHERE team_long_name=?", (fullname,)).fetchall()[0]
        team = Entity.Team(row[1], row[3], row[2])
        return team


def average(players):
    av_sum = 0
    num = 0
    for a in players:
        if a is not None:
            av_sum += a
            num += 1
    av_sum = av_sum / num

    return av_sum


class Match_Dao:
    def __init__(self, db_path="database.sqlite"):
        db_connection = sqlite3.connect(db_path)
        self.cursor = db_connection.cursor()

    def get_match_by_teams_season(self, home_team_id, away_team_id, season):
        row = self.cursor.execute("SELECT home_team_api_id,away_team_api_id,season,home_team_goal,away_team_goal,date "
                                  "FROM Match WHERE home_team_api_id=? AND away_team_api_id=?"
                                  " AND Match.season=?", (home_team_id, away_team_id, season)).fetchall()[0]

        match = Entity.Match(row[0], row[1], row[2], row[3], row[4], row[5])
        return match

    def get_last5_matches_of_team(self, team, date):

        row = self.cursor.execute("SELECT home_team_api_id,away_team_api_id,season,home_team_goal,away_team_goal,date "
                                  "FROM (SELECT * FROM Match WHERE away_team_api_id=? "
                                  "OR home_team_api_id=?) ORDER BY date DESC",
                                  (team.api_id, team.api_id)).fetchall()
        matches = []
        for i in row:
            if i[5] < date:
                matches.append(Entity.Match(i[0], i[1], i[2], i[3], i[4], i[5]))
            if len(matches) == 5: return matches
        return matches

    def get_players_func(self, match_id):
        row = self.cursor.execute("SELECT * FROM Match WHERE match_api_id=?", (match_id,)).fetchone()
        home_players = row[55:66]

        away_players = row[66:77]

        date = row[5]

        skills_away = []
        skills_home = []
        for x in home_players:
            a = self.cursor.execute("SELECT overall_rating,Player_Attributes.date FROM Player_Attributes"
                                    " WHERE date>? AND player_api_id=? ORDER BY date ASC",
                                    (date, x)).fetchall()
            if len(a) > 0:
                skills_home.append(a[0][0])
        for x in away_players:
            a = self.cursor.execute("SELECT overall_rating,date FROM Player_Attributes"
                                    " WHERE date>? AND player_api_id=? ORDER BY date ASC", (date, x)).fetchall()
            if len(a) > 0:
                skills_away.append(a[0][0])
        return average(skills_home) / average(skills_away)

    def get_statistics(self, team1, team2):
        row = self.cursor.execute("select home_team_api_id,away_team_api_id,home_team_goal,away_team_goal"
                                  " from Match WHERE (away_team_api_id=? and home_team_api_id=?)"
                                  " OR (home_team_api_id=? AND away_team_api_id=?)",(team1,team2,team1,team2))
        print row.fetchall()
