"""
QUESTION:
Implement a function `_get_mock_func` that takes an `operation_name` as input and returns the corresponding mock function from the `MOCK_OPERATIONS` dictionary if it is not disabled. The function should check the environment variable `MOCK_BOTO3_DISABLED_FUNCS` for a comma-separated list of disabled function names. If the operation is disabled or not found, return `None`.
"""

import os

def _get_mock_func(operation_name):
    MOCK_OPERATIONS = {
        'func1': 'mock_operation1',
        'func2': 'mock_operation2',
        'func3': 'mock_operation3'
    }
    
    disabled_funcs = os.environ.get('MOCK_BOTO3_DISABLED_FUNCS', '').split(',')
    for func, operation in MOCK_OPERATIONS.items():
        if func == operation_name and func not in disabled_funcs:
            return operation
    return None