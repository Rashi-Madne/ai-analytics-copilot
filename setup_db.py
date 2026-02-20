import sqlite3
import pandas as pd

print("Reading CSV...")

df = pd.read_csv("data.csv")   # make sure file name matches

print("Creating database...")

conn = sqlite3.connect("analytics.db")

df.to_sql("analytics", conn, if_exists="replace", index=False)

print("Database + table created successfully!")

conn.close()
