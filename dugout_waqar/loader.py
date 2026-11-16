import csv
from dugout_waqar.models import Player, FantasyTeam

def load_players(path):
    
    players = {}
    
    with open(path, newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            player = Player.form_row(row)
            players[player.player_id] = player
    return players

def team_from_row(row, players):
    """Return a FantasyTeam built from one row (a dict) of a teams CSV file.
    The CSV stores player ids such as "P012;P089", so we use the players
    dict to turn each id back into a real Player object.
    """
    team = FantasyTeam(row["team_name"], row["owner"])
    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])

    team.set_captain(players[row["captain"]], players[row["vice_captain"]])
    return team

def load_team(path, players):
    # Return the first team in a teams CSV file, or None if the file has no teams.
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            return team_from_row(row, players)  # return on the first row only
    return None

def load_teams(path, players):
    """Return a list of every team in a teams CSV file."""
    teams = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            teams.append(team_from_row(row, players))
    return teams
 
 
# main.py: change the import line at the top to
# from dugout_waqar.loader import load_players, load_teams
