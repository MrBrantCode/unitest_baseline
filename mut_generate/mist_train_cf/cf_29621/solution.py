"""
QUESTION:
Implement the `generate_sql_statements(migrations)` function, which takes a list of migration operations and returns a list of SQL statements that would apply those migrations to a database. Each migration operation is a tuple containing the operation type and relevant details. The supported operation types are `CreateTable`, `AlterTable`, and `AlterUniqueTogether`. The function should return SQL statements in the order that the migrations were provided. 

The `CreateTable` operation contains the table name and a list of column definitions. The `AlterTable` operation contains the table name and a list of alteration operations, where each alteration operation starts with the string 'ADD COLUMN'. The `AlterUniqueTogether` operation contains the table name and a list of column names that should have a unique constraint together.
"""

def generate_sql_statements(migrations):
    sql_statements = []
    for migration in migrations:
        if migration[0] == 'CreateTable':
            table_name, columns = migration[1], migration[2]
            columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])
            sql_statements.append(f'CREATE TABLE {table_name} ({columns_str});')
        elif migration[0] == 'AlterTable':
            table_name, alterations = migration[1], migration[2]
            for alteration in alterations:
                if alteration[0] == 'ADD COLUMN':
                    column_name, column_type = alteration[1], alteration[2]
                    sql_statements.append(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};')
        elif migration[0] == 'AlterUniqueTogether':
            table_name, unique_columns = migration[1], migration[2]
            columns_str = ', '.join(unique_columns)
            sql_statements.append(f'ALTER TABLE {table_name} ADD CONSTRAINT unique_{table_name} UNIQUE ({columns_str});')
    return sql_statements