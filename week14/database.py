import sqlite3

conn = sqlite3.connect("students.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
program TEXT NOT NULL
)
""")
conn.commit()
conn.close()