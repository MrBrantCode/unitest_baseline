"""
QUESTION:
Implement a `DatabaseTable` class with `add_field` and `generate_sql` methods. The `add_field` method should allow adding fields to the table with a name and a data type, and optionally mark the field as a primary key. The `generate_sql` method should return a string representing the SQL statement to create the table in a database. The SQL statement should include the table name, field names, data types, and primary key constraints. The class should be able to handle multiple fields and primary keys correctly.
"""

def create_database_table(table_name, fields):
    sql = f"CREATE TABLE {table_name} (\n"
    primary_keys = [field[0] for field in fields if len(field) > 2 and field[2]]
    for field in fields:
        if len(field) > 2 and field[2]:
            field_sql = f"    {field[0]} {field[1]} PRIMARY KEY"
        else:
            field_sql = f"    {field[0]} {field[1]}"
        sql += field_sql + ",\n"
    sql = sql.rstrip(",\n") 
    if primary_keys:
        sql += f",\n    PRIMARY KEY ({', '.join(primary_keys)})"
    sql += "\n);"
    return sql