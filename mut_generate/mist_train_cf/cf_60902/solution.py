"""
QUESTION:
Design a function named `factorial_tuple` that takes a tuple and a list as arguments. The function should calculate the factorial of each integer element in the tuple and append the results to the given list. The function should handle tuples containing zero and negative numbers, return an error message if the tuple is empty, and handle nested tuples up to three levels. The function should also return specific error messages for non-integer inputs and tuples with more than three levels of nesting.
"""

def factorial_tuple(tup, lst, depth=0, max_depth=3):
    """Compute factorial of each element in a given tuple and append to a list."""
    def factorial(n):
        """Return the factorial of a non-negative integer."""
        if n == 0: return 1
        fact = 1
        for i in range(1, n+1): fact *= i
        return fact

    def is_integer(n):
        """Return True if the input is an integer, False otherwise."""
        import numbers
        return isinstance(n, numbers.Integral)

    def tuple_depth(tup):
        """Return the depth of nesting in a tuple."""
        if isinstance(tup, tuple): 
            return 1 + max(tuple_depth(item) for item in tup)
        return 0

    if not tup: return "Error: Input tuple is empty"
    depth += 1
    for item in tup:
        if isinstance(item, tuple):
            if depth > max_depth: return "Error: Tuple nesting exceeds maximum depth"
            msg = factorial_tuple(item, lst, depth)
            if isinstance(msg, str): return msg  # if error message is returned
        else:
            if not is_integer(item): 
                return "Error: Non-integer input in tuple"
            if item < 0: 
                return "Error: Negative integer in tuple"
            lst.append(factorial(item))
    if depth == 1: return lst