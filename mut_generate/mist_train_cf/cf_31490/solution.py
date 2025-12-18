"""
QUESTION:
Write a function `parseSQLCreateTable` that takes a SQL code snippet for creating a table as input and returns a dictionary containing the table name, database name, and column names along with their data types. The SQL code snippet is a string of length between 1 and 1000, and the function should return a dictionary with the keys "database_name", "table_name", and "columns". The "columns" key should map to a list of dictionaries, each containing the keys "column_name" and "data_type".
"""

import re

def parseSQLCreateTable(sql_code: str) -> dict:
    pattern = r'CREATE TABLE IF NOT EXISTS (\w+)\.(\w+)\((.+)\);'
    match = re.match(pattern, sql_code)
    if match:
        database_name = match.group(1)
        table_name = match.group(2)
        columns_info = match.group(3)
        columns = re.findall(r'"(\w+)"\s+(\w+\(?\d*\)?)', columns_info)
        columns_data = [{"column_name": col[0], "data_type": col[1]} for col in columns]
        return {"database_name": database_name, "table_name": table_name, "columns": columns_data}
    else:
        return {}