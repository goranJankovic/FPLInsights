from db import get_db_connection

def create_players_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            second_name TEXT,
            team_id INTEGER,
            element_type INTEGER,
            now_cost REAL,
            total_points INTEGER,
            goals_scored INTEGER,
            assists INTEGER,
            clean_sheets INTEGER,
            selected_by_percent REAL,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
    ''')
    conn.commit()
    conn.close()

def save_players(players):
    conn = get_db_connection()
    c = conn.cursor()
    for player in players:
        selected_by_percent = float(player["selected_by_percent"]) if player["selected_by_percent"] else 0.0
        now_cost = float(player["now_cost"]) / 10 if player["now_cost"] else 0.0
        c.execute('''
            INSERT OR REPLACE INTO players (
                id, first_name, second_name, team_id, element_type, now_cost,
                total_points, goals_scored, assists, clean_sheets, selected_by_percent
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            player["id"], player["first_name"], player["second_name"], player["team"],
            player["element_type"], now_cost, player["total_points"],
            player["goals_scored"], player["assists"], player["clean_sheets"],
            selected_by_percent
        ))
    conn.commit()
    conn.close()
