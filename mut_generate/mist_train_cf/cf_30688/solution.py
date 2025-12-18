"""
QUESTION:
Create a function `format_sql_query` that formats a SQL query string by replacing placeholders with provided values while ensuring safety from SQL injection attacks. The function takes two parameters:
- `sql` (string): The original SQL query with placeholders for values.
- `values` (list, tuple, or single value): The values to be inserted into the SQL query.

The function should handle different types of SQL queries and values, including lists, tuples, and single values, and return the formatted SQL query string. The placeholders in the SQL query should be in the format `%s`.
"""

def format_sql_query(sql, values):
    if isinstance(values, (list, tuple)):
        formatted_values = tuple("'" + str(val) + "'" if isinstance(val, str) else str(val) for val in values)
    else:
        formatted_values = "'" + str(values) + "'" if isinstance(values, str) else str(values)
    
    formatted_sql = sql % formatted_values
    return formatted_sql