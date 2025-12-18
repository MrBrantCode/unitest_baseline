"""
QUESTION:
Implement the function `apply_migrations(migrations, schema)` that takes a list of migration operations `migrations` and applies them to a database schema `schema`. Each migration operation is a tuple of three elements: (operation_type, field_name, new_field_type), where operation_type is "AddField", "AlterField", or "RemoveField". Apply the migration operations to the schema in the order they appear in the list and return the final schema after applying all the migrations.
"""

def apply_migrations(migrations, schema):
    for operation, field_name, new_field_type in migrations:
        if operation == "AddField":
            schema[field_name] = new_field_type
        elif operation == "AlterField":
            if field_name in schema:
                schema[field_name] = new_field_type
        elif operation == "RemoveField":
            if field_name in schema:
                del schema[field_name]
    return schema