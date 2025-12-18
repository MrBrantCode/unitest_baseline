"""
QUESTION:
Implement a function `process_migrations(migrations)` that takes a list of migration operations as input, where each operation is a tuple containing the operation type ("CreateModel" or "DeleteModel") and the name of the model being affected. Return the final state of the database schema as a list of model names after applying all operations sequentially.
"""

def process_migrations(migrations):
    schema = set()
    for operation, model in migrations:
        if operation == "CreateModel":
            schema.add(model)
        elif operation == "DeleteModel":
            schema.discard(model)
    return list(schema)