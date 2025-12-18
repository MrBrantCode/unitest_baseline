"""
QUESTION:
Write a function called `calculate_nth_term` that determines the nth term in a geometric progression given the initial term `a` and the common ratio `r`. The function should return the nth term. Assume `a`, `r`, and `n` are integers and `n` is a positive integer greater than 0.
"""

def calculate_nth_term(a, r, n):
    """
    Calculate the nth term in a geometric progression.

    Parameters:
    a (int): The initial term.
    r (int): The common ratio.
    n (int): The position of the term in the sequence.

    Returns:
    int: The nth term in the sequence.
    """
    return a * (r ** (n - 1))