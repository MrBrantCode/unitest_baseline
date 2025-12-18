"""
QUESTION:
Implement the `compare_schemas` function that takes in two lists of database schemas, where each schema is a list of tables and each table is a dictionary containing the table name and its corresponding columns. The function should return a list of tuples representing the differences between the schemas. Each tuple should contain the table name and a string indicating the type of difference (e.g., "added column", "removed table", "modified column").
"""

def compare_schemas(schemas1, schemas2):
    differences = []

    table_names1 = {schema['table_name'] for schema in schemas1}
    table_names2 = {schema['table_name'] for schema in schemas2}
    added_tables = table_names2 - table_names1
    removed_tables = table_names1 - table_names2

    for table in added_tables:
        differences.append((table, "added table"))
    for table in removed_tables:
        differences.append((table, "removed table"))

    for schema1 in schemas1:
        for schema2 in schemas2:
            if schema1['table_name'] == schema2['table_name']:
                added_columns = set(schema2['columns']) - set(schema1['columns'])
                removed_columns = set(schema1['columns']) - set(schema2['columns'])
                modified_columns = set()
                for col in schema1['columns']:
                    if col in schema2['columns'] and schema1['columns'].index(col) != schema2['columns'].index(col):
                        modified_columns.add(col)
                for col in added_columns:
                    differences.append((schema1['table_name'], f"added column '{col}'"))
                for col in removed_columns:
                    differences.append((schema1['table_name'], f"removed column '{col}'"))
                for col in modified_columns:
                    differences.append((schema1['table_name'], f"modified column '{col}'"))

    return differences