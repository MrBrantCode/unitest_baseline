"""
QUESTION:
Create a function, `sum_sequence`, that takes an integer `N` as input and returns the sum of the sequence from 1 to `N` if `N` is positive, or the sum from `N` to 1 if `N` is negative, without using the built-in `sum` function.
"""

def sum_sequence(N):
    """
    Calculate the sum of a sequence from 1 to N if N is positive, 
    or from N to 1 if N is negative.

    Args:
    N (int): The input integer.

    Returns:
    int: The sum of the sequence.
    """
    if N > 0:
        return (N*(N+1))//2
    else:
        return (N*(N-1))//-2