"""
QUESTION:
Implement the function `apply_migrations(migrations, database_schema)` to apply a list of migration operations to a database schema. 

The function takes two parameters: 
- `migrations`, a list of tuples representing the migration operations, where each tuple contains four values: `operation_type`, `model_name`, `field_name`, and `new_field_type`. 
- `database_schema`, a dictionary representing the initial database schema, where the keys are model names and the values are lists of field names.

The function should return the modified database schema after applying all the migration operations. The operation types can be "AddField", "AlterField", or "DeleteField". The "AlterField" operation does not change the field name but updates the field type which is not reflected in the returned schema.
"""

def apply_migrations(migrations, database_schema):
    for operation, model_name, field_name, new_field_type in migrations:
        if operation == "AddField":
            if model_name in database_schema:
                database_schema[model_name].append(field_name)
            else:
                database_schema[model_name] = [field_name]
        elif operation == "AlterField":
            if model_name in database_schema and field_name in database_schema[model_name]:
                database_schema[model_name][database_schema[model_name].index(field_name)] = field_name
        elif operation == "DeleteField":
            if model_name in database_schema and field_name in database_schema[model_name]:
                database_schema[model_name].remove(field_name)
    return database_schema