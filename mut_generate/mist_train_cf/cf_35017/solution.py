"""
QUESTION:
Create a function `apply_migrations` that simulates the process of applying database migrations to a database schema. The function takes a list of migration operations as input, where each operation is a tuple of the form `(operation_type, model_name, field_name, field_type)`. The function applies each operation in the list to the database schema in the order they appear in the input list. The database schema is represented as a dictionary where the keys are model names and the values are lists of field names and types.

The function should support the following operation types:
- `AddField`: Add a new field to an existing model.
- `AlterField`: Alter the type of an existing field in a model.
- `CreateModel`: Create a new model with a single field.

The function should return the updated database schema after applying all the operations.

Function signature: 
`def apply_migrations(operations: List[Tuple[str, str, str, str]]) -> Dict[str, List[Tuple[str, str]]]`
"""

from typing import List, Tuple, Dict

def apply_migrations(operations: List[Tuple[str, str, str, str]]) -> Dict[str, List[Tuple[str, str]]]:
    schema = {}
    for operation in operations:
        operation_type, model_name, field_name, field_type = operation
        if operation_type == 'AddField':
            if model_name in schema:
                schema[model_name].append((field_name, field_type))
            else:
                schema[model_name] = [(field_name, field_type)]
        elif operation_type == 'AlterField':
            if model_name in schema:
                for i, (name, _) in enumerate(schema[model_name]):
                    if name == field_name:
                        schema[model_name][i] = (field_name, field_type)
                        break
        elif operation_type == 'CreateModel':
            schema[model_name] = [(field_name, field_type)]
    return schema