"""
QUESTION:
Write a function `extract_operations` that takes a list of strings representing compute template operations in the format "# [END operation_name]" as input, extracts the unique operation names, and returns them in lexicographically sorted order. The function should ignore any text outside the brackets and only consider the operation names inside the brackets.
"""

from typing import List

def extract_operations(operations: List[str]) -> List[str]:
    unique_operations = set()
    for operation in operations:
        operation_name = operation.split("[END ")[1].split(" ]")[0]
        unique_operations.add(operation_name)
    return sorted(list(unique_operations))