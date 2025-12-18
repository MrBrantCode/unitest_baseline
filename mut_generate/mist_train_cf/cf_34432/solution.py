"""
QUESTION:
Implement the function `parse_migration_operations(migration_file: str) -> List[str]` that takes a Django migration file as a string and returns a list of migration operation names present in the file. The migration file is in the standard Django migration file format and the operation names should be extracted from the `migrations` module.
"""

from typing import List
import re

def parse_migration_operations(migration_file: str) -> List[str]:
    operation_pattern = r'migrations\.(?:\w+)'
    operations = re.findall(operation_pattern, migration_file)
    operation_names = [op.split('.')[-1] for op in operations]
    return operation_names