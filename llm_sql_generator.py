import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(question, schema):

    prompt = f"""
You are a data analyst.

Convert this English question into SQL using the database schema.

Schema:
{schema}

Question:
{question}

Return ONLY SQL query.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
