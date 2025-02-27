import requests
from db import get_db_connection


def create_player_history_table():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS player_history;")

    c.execute('''
        CREATE TABLE IF NOT EXISTS player_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            gameweek INTEGER,
            total_points INTEGER,
            goals_scored INTEGER,
            assists INTEGER,
            clean_sheets INTEGER,
            opponent_team INTEGER,
            home_score INTEGER,
            away_score INTEGER,
            home BOOLEAN,
            bonus_points INTEGER,
            expected_goals REAL,
            expected_assists REAL,
            transfers_in INTEGER,
            transfers_out INTEGER,
            kickoff_time TEXT,
            FOREIGN KEY (player_id) REFERENCES players(id)
        )
    ''')
    conn.commit()
    conn.close()


def fetch_and_store_player_history():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("SELECT id FROM players")
    players = c.fetchall()

    for player in players:
        player_id = player[0]  # ID is equal with FPL player id
        url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/" # todo move this to fetch_data
        response = requests.get(url)

        if response.status_code == 200:
            player_data = response.json()
            for gw in player_data["history"]:
                home = gw.get("was_home", True)
                opponent_team = gw.get("opponent_team")
                home_score = gw.get("team_h_score")
                away_score = gw.get("team_a_score")
                bonus_points = gw.get("bonus", 0)
                expected_goals = float(gw.get("expected_goals", 0))
                expected_assists = float(gw.get("expected_assists", 0))
                transfers_in = gw.get("transfers_in", 0)
                transfers_out = gw.get("transfers_out", 0)
                kickoff_time = gw.get("kickoff_time")

                c.execute('''
                    INSERT OR REPLACE INTO player_history (
                        player_id, gameweek, total_points, goals_scored, assists, clean_sheets,
                        opponent_team, home_score, away_score, home, bonus_points,
                        expected_goals, expected_assists, transfers_in, transfers_out, kickoff_time
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    player_id, gw["round"], gw["total_points"], gw["goals_scored"], gw["assists"],
                    gw["clean_sheets"], opponent_team, home_score, away_score, home,
                    bonus_points, expected_goals, expected_assists, transfers_in, transfers_out, kickoff_time
                ))
        else:
            print(f"Error fetching data for player {player_id}")

    conn.commit()
    conn.close()
    print("Player history successfully updated!")