"""
QUESTION:
Create a function `count_migration_operations` that takes a list of database migration operations as strings and returns a dictionary where the keys are the unique operation types and the values are their corresponding counts. The operation type is the part of the string between "migrations." and the first opening parenthesis.
"""

from typing import List, Dict
import re

def count_migration_operations(operations: List[str]) -> Dict[str, int]:
    operation_counts = {}
    for operation in operations:
        operation_type = re.search(r'migrations\.(\w+)', operation).group(1)
        operation_counts[operation_type] = operation_counts.get(operation_type, 0) + 1
    return operation_counts