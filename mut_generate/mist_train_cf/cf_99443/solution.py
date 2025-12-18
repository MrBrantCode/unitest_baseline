"""
QUESTION:
Create a function named `generate_sql_statement` that generates a dynamic SQL statement to retrieve records from multiple tables. The function should accept three parameters: 
- `table_list`: a list of table names to join
- `join_conditions`: a list of join conditions
- `filter_conditions`: a dictionary of filter conditions (key = column name, value = filter value)

The function should return a string representing the generated SQL statement with the specified join conditions and filter conditions. The SQL statement should include the ability to filter results using the provided filter conditions. The function should handle cases where no filter conditions are provided.
"""

def generate_sql_statement(table_list, join_conditions, filter_conditions):
    # Generate SELECT statement
    select_statement = "SELECT * FROM "
    # Add table names to SELECT statement
    for i, table_name in enumerate(table_list):
        if i == 0:
            select_statement += table_name
        else:
            select_statement += " JOIN " + table_name
    # Generate JOIN statement
    join_statement = " ON ".join(join_conditions)
    # Generate WHERE statement
    where_conditions = []
    for column_name, filter_value in filter_conditions.items():
        where_conditions.append(column_name + " = " + filter_value)
    where_statement = " AND ".join(where_conditions)
    # Combine all statements into final SQL statement
    sql_statement = select_statement + " ON " + join_statement
    if filter_conditions:
        sql_statement += " WHERE " + where_statement
    return sql_statement