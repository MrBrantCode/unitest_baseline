"""
QUESTION:
Create a function named `create_sql_query` that generates a SQL query string to extract data from a table. The function should take four parameters: `table`, `secondary_table`, `condition`, and `sorting`. 

`table` is the name of the primary table to extract data from, and it is a required parameter. 
`secondary_table` is the name of the secondary table to join with the primary table, and it is an optional parameter. If provided, the function should perform an inner join on `department_id`. 
`condition` is a string representing the condition/filter to apply to the query, and it is an optional parameter. If provided, the function should add the condition after the `WHERE` clause. 
`sorting` is a string representing the column to sort the data by, and it is an optional parameter. If provided, the function should add the sorting clause after the `ORDER BY` clause.

The function should return the generated SQL query string.
"""

def create_sql_query(table, secondary_table=None, condition=None, sorting=None):
    query = f"SELECT * FROM {table}"
    
    if secondary_table:
        query += f" JOIN {secondary_table} ON {table}.department_id = {secondary_table}.department_id"

    if condition:
        query += f" WHERE {condition}"

    if sorting:
        query += f" ORDER BY {sorting}"
    
    return query