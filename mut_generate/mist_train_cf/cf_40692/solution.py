"""
QUESTION:
Create a function `count_migration_operations(operations: List[str]) -> Dict[str, int]` that takes a list of migration operations as strings and returns a dictionary containing the count of each type of operation. The operation strings are in the format "migrations.OperationName(model_name='ModelName', ...)" and the function should ignore case when counting the operation types. The keys of the dictionary should be the lowercase operation names, and the values should be the count of each operation type.
"""

from typing import List, Dict

def count_migration_operations(operations: List[str]) -> Dict[str, int]:
    operation_counts = {}
    for operation in operations:
        operation_name = operation.split('(')[0].split('.')[-1].lower()
        operation_counts[operation_name] = operation_counts.get(operation_name, 0) + 1
    return operation_counts