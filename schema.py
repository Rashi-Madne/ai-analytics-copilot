import sqlite3

print("Connecting to DB...")

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

print("Fetching schema...")

cursor.execute("PRAGMA table_info(analytics)")
columns = cursor.fetchall()

print("Number of columns:", len(columns))

for col in columns:
    print(col)

conn.close()

