import sqlite3

def run_query(query):
    try:
        conn = sqlite3.connect("analytics.db")
        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()
        return results

    except Exception as e:
        return f"SQL Error: {str(e)}"
