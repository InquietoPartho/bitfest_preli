import sqlite3
import os

def create_db():
    # Path to the database file
    db_path = 'database/db.sqlite3'

    # Check if the database already exists and delete it if it does (for clean restart)
    if os.path.exists(db_path):
        os.remove(db_path)

    # Create a new database connection and cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity TEXT NOT NULL
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
