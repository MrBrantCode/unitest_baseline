"""
QUESTION:
Write a function named master_theorem that analyzes the time complexity of a recursive algorithm using the Master Theorem. The function should take as input the parameters a, b, and d from the recurrence relation T(n) = aT(n/b) + O(n^d) and return the time complexity. Assume a, b, and d are all positive integers and b > 1.
"""

def master_theorem(a, b, d):
    """
    Analyzes the time complexity of a recursive algorithm using the Master Theorem.

    Args:
    a (int): The number of subproblems in the recursion.
    b (int): The base of the subproblem size.
    d (int): The exponent of n in the non-recursive part.

    Returns:
    str: The time complexity of the recursive algorithm.
    """
    if a < b**d:
        return f"O(n^{d})"
    elif a == b**d:
        return f"O(n^{d} log n)"
    else:
        return f"O(n^(log_{b} {a}))"