"""
QUESTION:
Design a function named `factorial_tuple` that calculates the factorial of each element in a given tuple and appends the results to a specific list. The function should handle tuples containing zero and negative numbers, and return an error message "Error: Tuple is empty" if the tuple is empty. The function should also handle tuples within tuples (nested tuples) and calculate the factorial for each number in these nested tuples, as well as tuples within tuples within tuples (deeply nested tuples). Additionally, the function should handle non-integer inputs and return a specific error message for this type of error.
"""

def factorial_tuple(tup, lst):
    if not tup:
        return "Error: Tuple is empty"
    for i in tup:
        if isinstance(i, tuple):
            result = factorial_tuple(i, lst)
            if isinstance(result, str):
                return result
        else:
            if not isinstance(i, int) or i < 0:
                return f"Error: Invalid input '{i}' in tuple"
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            lst.append(fact)
    return lst