import sys
from db import get_db_connection

def get_player_history_from_db(player_id):
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''
        SELECT gameweek, total_points, goals_scored, assists, clean_sheets, home_score, away_score, home, bonus_points,
               expected_goals, expected_assists, transfers_in, transfers_out, kickoff_time, opponent_team
        FROM player_history WHERE player_id = ? ORDER BY gameweek
    ''', (player_id,))

    history = c.fetchall()

    opponent_names = {}
    opponent_ids = [row[14] for row in history if row[14] is not None]
    if opponent_ids:
        c.execute(f"SELECT id, name FROM teams WHERE id IN ({','.join('?' * len(opponent_ids))})", opponent_ids)
        opponent_names = dict(c.fetchall())

    conn.close()

    if not history:
        print(f"No history found for player {player_id}")
        return

    print(
        "GW | Points | Goals | Assists | CS | Home | H-Score | A-Score |     Opponent    | Bonus |  xG  |  xA  | Transfers In | Transfers Out| Kickoff Time")
    print("-" * 140)
    for row in history:
        gameweek, points, goals, assists, clean_sheets, home_score, away_score, home, bonus_points, xG, xA, transfers_in, transfers_out, kickoff_time, opponent_team = row

        xG = 0.00 if xG is None else xG
        xA = 0.00 if xA is None else xA

        opponent_name = opponent_names.get(opponent_team, "Unknown")

        print(
            f"{gameweek:>2} | {points:>6} | {goals:>5} | {assists:>7} | {clean_sheets:>2} | {home:>4} | {home_score:>7} | {away_score:>7} | {opponent_name:>15} | {bonus_points:>5} | {xG:>4.2f} | {xA:>4.2f} | {transfers_in:>12} | {transfers_out:>12} | {kickoff_time}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_player_history.py <player_id>")
        sys.exit(1)

    try:
        player_id = int(sys.argv[1])
        get_player_history_from_db(player_id)
    except ValueError:
        print("Error: Player ID must be an integer.")
        sys.exit(1)
