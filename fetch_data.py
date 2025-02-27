import requests

FPL_BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
FPL_FIXTURES_URL = "https://fantasy.premierleague.com/api/fixtures/"

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fetch error: {response.status_code}")
        return None

def get_fpl_data():
    return fetch_data(FPL_BOOTSTRAP_URL)

def get_fixtures():
    return fetch_data(FPL_FIXTURES_URL)
