from db import get_db_connection

def create_events_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            name TEXT,
            deadline_time TEXT,
            finished INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_events(events):
    conn = get_db_connection()
    c = conn.cursor()
    for event in events:
        c.execute('''
            INSERT OR REPLACE INTO events (id, name, deadline_time, finished)
            VALUES (?, ?, ?, ?)
        ''', (
            event["id"], event["name"], event["deadline_time"], event["finished"]
        ))
    conn.commit()
    conn.close()
