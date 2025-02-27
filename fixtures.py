from db import get_db_connection

def create_fixtures_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS fixtures (
            id INTEGER PRIMARY KEY,
            event INTEGER,
            home_team INTEGER,
            away_team INTEGER,
            home_team_score INTEGER,
            away_team_score INTEGER,
            kickoff_time TEXT,
            FOREIGN KEY (home_team) REFERENCES teams(id),
            FOREIGN KEY (away_team) REFERENCES teams(id)
        )
    ''')
    conn.commit()
    conn.close()

def save_fixtures(fixtures):
    conn = get_db_connection()
    c = conn.cursor()
    for fixture in fixtures:
        c.execute('''
            INSERT OR REPLACE INTO fixtures (
                id, event, home_team, away_team, home_team_score, away_team_score, kickoff_time
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            fixture["id"], fixture.get("event"), fixture["team_h"], fixture["team_a"],
            fixture.get("team_h_score"), fixture.get("team_a_score"), fixture.get("kickoff_time")
        ))
    conn.commit()
    conn.close()
