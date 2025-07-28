# FPLInsights 📊

A Python project for analyzing data retrieved from the **Fantasy Premier League API**.\
It fetches **teams, players, fixtures, and statistics** and stores them in an **SQLite database**.

## 🚀 How to Run the Project

Clone the repository:

```bash
git clone https://github.com/goranJankovic/FPLInsights.git
cd FPLInsights
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main script to fetch and store data:

```bash
python main.py
```

Analyze the data using SQLite:

```bash
sqlite3 fpl_data.db
```

## 📦 Requirements

- Python 3.8+
- SQLite3 (built-in with Python)
- Required Python libraries (installed via `requirements.txt`):
  ```
  requests
  sqlite3
  tabulate
  notebook
  ```
  Install with:
  ```bash
  pip install -r requirements.txt
  ```

## ✅ Features

👉 Fetches teams, players, fixtures, and statistics\
👉 Stores data in an SQLite database\
👉 Supports SQL queries for analysis\
👉 Simple and easy-to-use structure

## 🔍 Example Queries

After fetching data, you can run SQL queries using:

```bash
sqlite3 fpl_data.db
```

Get all players with their teams and positions:

```sql
SELECT players.first_name, players.second_name, teams.name AS team, element_types.name AS position
FROM players
         JOIN teams ON players.team_id = teams.id
         JOIN element_types ON players.element_type = element_types.id;
```

Top 10 players by total points:

```sql
SELECT first_name, second_name, total_points
FROM players
ORDER BY total_points DESC
LIMIT 10;
```

## 🔍 Example Player History Preview

```bash
python get_player_history.py 328 // Salah id
```
```
GW | Points | Goals | Assists | CS | Home | H-Score | A-Score | Bonus | xG | xA | Transfers In | Transfers Out | Kickoff Time
--------------------------------------------------------------------------------------------------------------------------------------------
 1 |     14 |     1 |       1 |  1 |    0 |       0 |       2 |     3 | 0.70 | 0.15 |            0 |            0 | 2024-08-17T11:30:00Z
 2 |     10 |     1 |       0 |  1 |    1 |       2 |       0 |     2 | 0.50 | 0.25 |       262302 |        64190 | 2024-08-25T15:30:00Z
 3 |     17 |     1 |       2 |  1 |    0 |       0 |       3 |     3 | 0.50 | 0.63 |       308526 |       186127 | 2024-09-01T15:00:00Z
```

## 📊 Jupyter Notebook Support
You can also explore and analyze FPL data interactively using Jupyter Notebooks.

```jupyter notebook```

An example notebook is included:

```fpl_query.ipynb```


### 🔍 Example Jupyter Output Preview

![Top Players Preview](assets/top_players.png)

This notebook allows you to:

Query fpl_data.db using SQL

Load results into pandas.DataFrame

Display formatted tables using tabulate

Prepare for visualizations with matplotlib or seaborn (optional)

## 📝 Future Improvements

🚀 Adding advanced data visualization\
🚀 Creating a REST API to serve data

💡 **Contributions are welcome!** Feel free to fork, improve, and submit pull requests.

📞 **GitHub Repository:** [FPLInsights](https://github.com/goranJankovic/FPLInsights)

🚀 Enjoy FPL data insights! 🏆


