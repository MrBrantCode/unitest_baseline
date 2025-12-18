"""
QUESTION:
Implement a Python function named `process_functions` that takes a dictionary `functions` and a list `input_values` as arguments. The `functions` dictionary contains function names as keys and the corresponding functions as values. Each function can take either one or two arguments and returns a single value. The function should return a new dictionary where the keys are the function names and the values are the results of applying the functions to the input values. The function should handle both lambda functions and built-in functions.
"""

def process_functions(functions, input_values):
    result_dict = {}
    for func_name, func in functions.items():
        if isinstance(func, type(lambda: 0)):
            if func.__code__.co_argcount == 1:
                result_dict[func_name] = func(input_values[0])
            elif func.__code__.co_argcount == 2:
                result_dict[func_name] = func(*input_values)
        else:
            result_dict[func_name] = func(*input_values)
    return result_dict