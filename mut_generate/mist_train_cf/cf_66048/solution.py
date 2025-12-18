"""
QUESTION:
Design a function named `factorial_tuple` that takes two parameters: a tuple `tup` and a list `lst`. The function should calculate the factorial of each integer element in `tup` (including those in nested tuples) and append the results to `lst`. The function must handle the following restrictions and edge cases: 
- If `tup` is not a tuple, return the error message "Error: Not a tuple."
- If `tup` is empty, return the error message "Error: Tuple is empty."
- If `tup` contains a negative integer, return the error message "Error: Negative number in tuple."
- If `tup` contains a non-integer element, return the error message "Error: Tuple contains non-integer element."
- The function should be able to handle nested tuples.
"""

import math

def factorial_tuple(tup, lst):
    if type(tup) != tuple:
        return 'Error: Not a tuple.'

    if not tup:
        return "Error: Tuple is empty."
    
    for i in tup:
        if isinstance(i, tuple):
            error_message = factorial_tuple(i, lst)
            if error_message:
                return error_message
        elif isinstance(i, int):
            if i < 0:
                return "Error: Negative number in tuple."
            else:
                lst.append(math.factorial(i)) 
        else:
            return 'Error: Tuple contains non-integer element.'