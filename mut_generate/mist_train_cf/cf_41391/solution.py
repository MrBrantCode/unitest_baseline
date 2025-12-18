"""
QUESTION:
Create a Python function named `generate_migration_script` that generates a migration script to transition a database from a current state to a desired state. The function takes two parameters: `current_state` and `desired_state`, each represented as a list of tuples, where each tuple contains a table name and a list of column names. The function should return a string representing the migration script, with SQL commands separated by semicolons.

The SQL commands should be in the following format: `CREATE TABLE table_name (column1 datatype, column2 datatype, ...);`, `ALTER TABLE table_name ADD column_name datatype;`, `ALTER TABLE table_name DROP COLUMN column_name;`, and `DROP TABLE table_name;`. Assume that the input lists are non-empty and that the table and column names are unique within each list.
"""

def generate_migration_script(current_state, desired_state):
    migration_script = ""

    # Tables to be created
    for table, columns in desired_state:
        if table not in [t[0] for t in current_state]:
            migration_script += f"CREATE TABLE {table} ({', '.join(columns)});\n"

    # Tables to be dropped
    for table, _ in current_state:
        if table not in [t[0] for t in desired_state]:
            migration_script += f"DROP TABLE {table};\n"

    # Columns to be added
    for table, columns in desired_state:
        if table in [t[0] for t in current_state]:
            current_columns = set(current_state[[t[0] for t in current_state].index(table)][1])
            for column in columns:
                if column not in current_columns:
                    migration_script += f"ALTER TABLE {table} ADD {column} datatype;\n"

    # Columns to be dropped
    for table, columns in current_state:
        if table in [t[0] for t in desired_state]:
            desired_columns = set(desired_state[[t[0] for t in desired_state].index(table)][1])
            for column in columns:
                if column not in desired_columns:
                    migration_script += f"ALTER TABLE {table} DROP COLUMN {column};\n"

    return migration_script