import pandas as pd
from sqlalchemy import create_engine

def read_query(query_name):
    with open("queries.sql", 'r') as file:
        content = file.read()

    queries = [q.strip() for q in content.split('--@name:')]
    for q in queries:
        lines = q.split('\n', 1)
        name = lines[0].strip()
        query = lines[1].strip() if len(lines) > 1 else ''
        if name == query_name:
            return query

    raise ValueError(f"Query with name '{query_name}' not found in the file.")

def query(query_name):
    connection_uri = "postgresql+psycopg2://postgres:password@localhost:5432/personal_finance_dashboard"
    query = read_query(query_name)
    db_engine = create_engine(connection_uri)
    df = pd.read_sql(query, db_engine)
    return df