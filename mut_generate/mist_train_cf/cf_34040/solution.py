"""
QUESTION:
Implement a function `parse_migration_operations(operations)` that takes a list of migration operations as input. Each operation is a tuple containing the operation type, model name, field name, field type, and default value. The function should return a dictionary where the keys are the model names and the values are lists of tuples containing the field name, field type, and default value. The operation type can be either "migrations.AlterField" or "migrations.CreateModel".
"""

from typing import List, Tuple, Dict

def parse_migration_operations(operations: List[Tuple[str, str, str, str, str]]) -> Dict[str, List[Tuple[str, str, str]]]:
    parsed_info = {}
    for operation in operations:
        operation_type, model_name, field_name, field_type, default_value = operation
        if model_name in parsed_info:
            parsed_info[model_name].append((field_name, field_type, default_value))
        else:
            parsed_info[model_name] = [(field_name, field_type, default_value)]
    return parsed_info