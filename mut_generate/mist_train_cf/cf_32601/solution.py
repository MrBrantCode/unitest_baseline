"""
QUESTION:
Create a function `generate_create_table_query` that takes a list of dictionaries, where each dictionary represents a column and its properties (name, data type, primary key status, uniqueness, and nullability), and returns a SQL query to create a table named "table_name" based on the given column specifications. The function should handle optional properties and generate the correct SQL constraints accordingly.
"""

def generate_create_table_query(columns: list) -> str:
    query = "CREATE TABLE table_name (\n"
    for column in columns:
        query += f"    {column['name']} {column['data_type']}"
        if column.get('primary_key'):
            query += " PRIMARY KEY"
        if column.get('unique'):
            query += " UNIQUE"
        if column.get('nullable') is False:
            query += " NOT NULL"
        query += ",\n"
    query = query.rstrip(",\n") + "\n);"
    return query