"""
QUESTION:
Create a function named `generate_query` that takes three parameters: `table_name`, `num_columns`, and `condition`. The function should return a SQL query as a string that selects all columns from the specified table where the column names follow the pattern "column_<number>" and the data is filtered based on the provided condition. The number of columns and the table name should be dynamic, and the condition should be a string representing a valid SQL WHERE clause.
"""

def generate_query(table_name, num_columns, condition):
    # Generate the column names dynamically
    columns = [f"column_{i+1}" for i in range(num_columns)]
    
    # Create the SELECT statement
    select_statement = "SELECT " + ", ".join(columns) + " FROM " + table_name
    
    # Create the WHERE clause
    where_clause = " WHERE " + condition
    
    # Concatenate the SELECT statement and WHERE clause
    query = select_statement + where_clause
    
    return query