"""
QUESTION:
Write a function `process_operations` that takes a list of tuples as input, where each tuple contains a string representing a function name, another string representing an operation ("one", "sqrt", or "square"), and an integer representing a value. The function should return a dictionary with the function names as keys and a list of results of the operations as values. If an operation is "one", the value is returned as is. If the operation is "sqrt", the square root of the value is returned. If the operation is "square", the square of the value is returned.
"""

import math

def process_operations(tuples_list):
    results = {}
    for item in tuples_list:
        function_name, operation, value = item
        if function_name in results:
            if operation == "one":
                results[function_name].append(value)
            elif operation == "sqrt":
                results[function_name].append(round(math.sqrt(value), 3))
            elif operation == "square":
                results[function_name].append(value ** 2)
        else:
            if operation == "one":
                results[function_name] = [value]
            elif operation == "sqrt":
                results[function_name] = [round(math.sqrt(value), 3)]
            elif operation == "square":
                results[function_name] = [value ** 2]
    return results