from db import get_db_connection

def create_elements_types_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS element_types (
          id INTEGER PRIMARY KEY,
          name TEXT
      )
      ''')
    conn.commit()
    conn.close()

def save_element_types(element_types):
    conn = get_db_connection()
    c = conn.cursor()
    for et in element_types:
        c.execute(
            "INSERT OR REPLACE INTO element_types (id, name) VALUES (?, ?)",
            (et["id"], et["plural_name"])
        )
    conn.commit()
    conn.close()