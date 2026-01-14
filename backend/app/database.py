import psycopg2
import os

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "ml"),
        user=os.getenv("DB_USER", "ml"),
        password=os.getenv("DB_PASSWORD", "ml")
    )

