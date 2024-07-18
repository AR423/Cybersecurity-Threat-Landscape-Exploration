import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()

# Create tables for each URL
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Associated_groups TEXT,
    Name TEXT,
    Description TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS softwares (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Associated_softwares TEXT,
    Name TEXT,
    Description TEXT,
    Type TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS techniques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Description TEXT,
    Type TEXT
)
''')

conn.commit()
conn.close()
