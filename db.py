import sqlite3

DB_NAME = "fpl_data.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)
