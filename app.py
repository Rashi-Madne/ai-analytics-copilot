from sql_generator import generate_sql
from database_engine import run_query

# Load schema
with open("schema_text.txt", "r") as f:
    schema = f.read()

def main():
    question = input("Ask your data question: ")

    sql_query = generate_sql(question, schema)
    print("\nGenerated SQL:")
    print(sql_query)

    results = run_query(sql_query)
    print("\nQuery Results:")
    print(results)

if __name__ == "__main__":
    main()
