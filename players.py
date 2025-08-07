from prompt_toolkit.utils import to_float

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
            minutes INTEGER,
            form REAL,
            points_per_game REAL,
            status TEXT,
            chance_of_playing_next_round INTEGER,
            transfers_in_event INTEGER,
            transfers_out_event INTEGER,
            in_dreamteam BOOLEAN,
            saves INTEGER,
            yellow_cards INTEGER,
            red_cards INTEGER,
            bonus INTEGER,
            bps INTEGER,
            influence REAL,
            creativity REAL,
            threat REAL,
            ict_index REAL,
            expected_goals REAL,
            expected_assists REAL,
            expected_goal_involvements REAL,
            expected_goals_conceded REAL,
            expected_goals_per_90 REAL,
            saves_per_90 REAL,
            expected_assists_per_90 REAL,
            expected_goal_involvements_per_90 REAL,
            expected_goals_conceded_per_90 REAL,
            goals_conceded_per_90 REAL,
            starts INTEGER,
            starts_per_90 REAL,
            clean_sheets_per_90 REAL,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
    ''')
    conn.commit()
    conn.close()

def save_players(players):
    conn = get_db_connection()
    c = conn.cursor()

    for player in players:
        values = (
            player["id"],
            player["first_name"],
            player["second_name"],
            player["team"],
            player["element_type"],
            float(player["now_cost"]) / 10,
            player["total_points"],
            player["goals_scored"],
            player["assists"],
            player["clean_sheets"],
            to_float(player["selected_by_percent"]),
            player["minutes"],
            to_float(player["form"]),
            to_float(player["points_per_game"]),
            player["status"],
            player["chance_of_playing_next_round"],
            player["transfers_in_event"],
            player["transfers_out_event"],
            bool(player["in_dreamteam"]),
            player["saves"],
            player["yellow_cards"],
            player["red_cards"],
            player["bonus"],
            player["bps"],
            to_float(player["influence"]),
            to_float(player["creativity"]),
            to_float(player["threat"]),
            to_float(player["ict_index"]),
            to_float(player["expected_goals"]),
            to_float(player["expected_assists"]),
            to_float(player["expected_goal_involvements"]),
            to_float(player["expected_goals_conceded"]),
            to_float(player["expected_goals_per_90"]),
            to_float(player["saves_per_90"]),
            to_float(player["expected_assists_per_90"]),
            to_float(player["expected_goal_involvements_per_90"]),
            to_float(player["expected_goals_conceded_per_90"]),
            to_float(player["goals_conceded_per_90"]),
            player["starts"],
            to_float(player["starts_per_90"]),
            to_float(player["clean_sheets_per_90"]),
        )

        c.execute(f'''
            INSERT OR REPLACE INTO players (
                id, first_name, second_name, team_id, element_type, now_cost,
                total_points, goals_scored, assists, clean_sheets, selected_by_percent,
                minutes, form, points_per_game, status, chance_of_playing_next_round,
                transfers_in_event, transfers_out_event, in_dreamteam, saves,
                yellow_cards, red_cards, bonus, bps, influence, creativity, threat,
                ict_index, expected_goals, expected_assists, expected_goal_involvements,
                expected_goals_conceded, expected_goals_per_90, saves_per_90,
                expected_assists_per_90, expected_goal_involvements_per_90,
                expected_goals_conceded_per_90, goals_conceded_per_90, starts,
                starts_per_90, clean_sheets_per_90
            ) VALUES ({','.join(['?'] * len(values))})
        ''', values)

    conn.commit()
    conn.close()
