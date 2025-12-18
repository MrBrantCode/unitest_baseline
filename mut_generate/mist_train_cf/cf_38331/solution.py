"""
QUESTION:
Create a function `execute_functions` that takes a list of tuples, where each tuple contains a function and its arguments. The function should execute each function with its corresponding arguments, handling any exceptions that may occur. If an exception is caught, the function should set a flag `reconnect` to `False` and continue to the next function. If no exceptions occur, the function should set `reconnect` to `True` and return the result of the last executed function. The function should handle exceptions of type `Exception`.
"""

from typing import List, Tuple, Callable, Any

def execute_functions(functions: List[Tuple[Callable, Tuple]]) -> Any:
    reconnect = True
    result = None
    for func, args in functions:
        try:
            result = func(*args)
        except Exception as err:
            reconnect = False
    return result if reconnect else None