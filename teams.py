from db import get_db_connection

def create_teams_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            short_name TEXT,
            strength INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_teams(teams):
    conn = get_db_connection()
    c = conn.cursor()
    for team in teams:
        c.execute('''
            INSERT OR REPLACE INTO teams (id, name, short_name, strength)
            VALUES (?, ?, ?, ?)
        ''', (team["id"], team["name"], team["short_name"], team["strength"]))
    conn.commit()
    conn.close()
