"""
QUESTION:
Write a Python function named `T` to express the running time of a recursive algorithm on an input of size `n`. The function should follow a recurrence relation where `T(n) = a*T(n/b) + f(n)`, where `a` is the number of subproblems, `b` is the factor by which the problem size decreases in each recursive call, and `f(n)` is the cost to break the problem into subproblems and merge the results.
"""

def T(n, a, b, f):
    """
    This function calculates the running time of a recursive algorithm on an input of size n.
    
    Parameters:
    n (int): The size of the input.
    a (int): The number of subproblems.
    b (int): The factor by which the problem size decreases in each recursive call.
    f (function): The cost to break the problem into subproblems and merge the results.

    Returns:
    float: The running time of the algorithm.
    """
    # Base case: if n is 1, return f(n)
    if n == 1:
        return f(n)
    # Recursive case: T(n) = a*T(n/b) + f(n)
    else:
        return a * T(n // b, a, b, f) + f(n)