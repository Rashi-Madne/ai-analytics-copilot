import sqlite3

def run_query(query):
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results


if __name__ == "__main__":
    q = "SELECT Product, SUM(Sales) FROM analytics GROUP BY Product ORDER BY SUM(Sales) DESC LIMIT 5"
    print(run_query(q))
