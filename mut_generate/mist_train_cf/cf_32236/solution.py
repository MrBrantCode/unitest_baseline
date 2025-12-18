"""
QUESTION:
Implement a function `convert_pg_array(pg_array)` that converts a one-dimensional PostgreSQL array-string to a Python list. The input PostgreSQL array-string is a comma-separated string enclosed in curly braces. If the input is not a string, the function should return the input as is.
"""

def convert_pg_array(pg_array):
    if not isinstance(pg_array, (str,)):
        return pg_array
    return [x.strip() for x in pg_array.strip("{}").split(",")]