import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY,
balance INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS codes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product TEXT,
code TEXT,
status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
product TEXT,
amount INTEGER,
status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS giftcodes(
code TEXT,
balance INTEGER,
max_users INTEGER,
used INTEGER
)
""")

conn.commit()
