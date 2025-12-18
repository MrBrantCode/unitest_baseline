"""
QUESTION:
Implement a function `count_migration_operations(operations)` that takes a list of migration operations as input and returns a dictionary containing the count of each type of operation. The dictionary should have the operation type as keys and the count of each type as values. Each operation is an instance of a migration class, and the function should identify the type of each operation using the `__name__` attribute of the operation's class. The function should be able to handle a list of any length and any number of operation types.
"""

def count_migration_operations(operations):
    operation_counts = {}
    for operation in operations:
        operation_type = type(operation).__name__
        operation_counts[operation_type] = operation_counts.get(operation_type, 0) + 1
    return operation_counts