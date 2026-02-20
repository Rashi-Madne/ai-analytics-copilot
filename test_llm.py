from llm_sql_generator import generate_sql

schema = open("schema_text.txt").read()

question = "top 5 products by sales"

sql = generate_sql(question, schema)

print("Generated SQL:")
print(sql)

