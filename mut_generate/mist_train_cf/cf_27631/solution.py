"""
QUESTION:
Create a Python function `apply_migrations` that takes an initial database schema and a list of migration operations as input, and returns the final database schema after applying all the migration operations. The initial database schema is a dictionary where keys are model names and values are lists of field names. The migration operations are a list of tuples containing the model name, operation type ("add", "remove", "modify"), and the field name. The function should handle the removal of fields from the database schema as well as other types of migration operations.
"""

def apply_migrations(initial_schema, migration_operations):
    schema = initial_schema.copy()
    for model, operation, field in migration_operations:
        if operation == 'remove':
            if field in schema.get(model, []):
                schema[model].remove(field)
        elif operation == 'add':
            if model in schema:
                schema[model].append(field)
            else:
                schema[model] = [field]
        elif operation == 'modify':
            if field in schema.get(model, []):
                # Perform modification operation (not specified in the given example)
                pass
    return schema