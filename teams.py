from db import get_db_connection


def parse_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def create_teams_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
              CREATE TABLE teams
              (
                  id                    INTEGER PRIMARY KEY,
                  code                  INTEGER,
                  name                  TEXT,
                  short_name            TEXT,
                  strength              INTEGER,
                  strength_overall_home INTEGER,
                  strength_overall_away INTEGER,
                  strength_attack_home  INTEGER,
                  strength_attack_away  INTEGER,
                  strength_defence_home INTEGER,
                  strength_defence_away INTEGER,
                  form                  REAL,
                  draw                  INTEGER,
                  win                   INTEGER,
                  loss                  INTEGER,
                  points                INTEGER,
                  position              INTEGER,
                  played                INTEGER
              );
              ''')
    conn.commit()
    conn.close()


def save_teams(teams):
    conn = get_db_connection()
    c = conn.cursor()
    for t in teams:
        c.execute("""
                  INSERT INTO teams (id, code, name, short_name, strength,
                                     strength_overall_home, strength_overall_away,
                                     strength_attack_home, strength_attack_away,
                                     strength_defence_home, strength_defence_away,
                                     form, draw, win, loss, points, position, played)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                  """, (
                      t["id"],
                      t["code"],
                      t["name"],
                      t["short_name"],
                      t["strength"],
                      t["strength_overall_home"],
                      t["strength_overall_away"],
                      t["strength_attack_home"],
                      t["strength_attack_away"],
                      t["strength_defence_home"],
                      t["strength_defence_away"],
                      parse_float(t["form"]),
                      t["draw"],
                      t["win"],
                      t["loss"],
                      t["points"],
                      t["position"],
                      t["played"]
                  ))
    conn.commit()
    conn.close()
