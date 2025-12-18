"""
QUESTION:
Create a recursive function `recursive_func(n)` that takes a nonnegative integer `n` as input and returns a result. The function should handle potential exceptions such as non-integer inputs or negative numbers, and should follow proper recursive function syntax.
"""

def recursive_func(n):
    # Testing if the provided argument is an integer and greater than or equal to 0
    if not isinstance(n, int) or n < 0:
        print('Please provide a nonnegative integer.')
        return None 

    if n <= 1:
        return n
    else:
        return recursive_func(n - 2) + recursive_func(n - 1)