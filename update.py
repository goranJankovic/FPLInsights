from fetch_data import get_fpl_data, get_fixtures
from player_history import create_player_history_table, fetch_and_store_player_history
from teams import create_teams_table, save_teams
from players import create_players_table, save_players
from fixtures import create_fixtures_table, save_fixtures
from events import create_events_table, save_events


def update_fpl_data():
    print("Fetch FPL data...")
    fpl_data = get_fpl_data()
    fixtures = get_fixtures()

    print("Updating...")
    create_teams_table()
    save_teams(fpl_data["teams"])

    create_players_table()
    save_players(fpl_data["elements"])

    create_fixtures_table()
    save_fixtures(fixtures)

    create_events_table()
    save_events(fpl_data["events"])

    print("Updating player history...")
    create_player_history_table()
    fetch_and_store_player_history()

print("Update done")

if __name__ == "__main__":
    update_fpl_data()
