"""
QUESTION:
Write a function `count_fractions(n)` that takes an integer `n` as input and returns the number of fractions that lie between `1/2` and `2/3` in the sorted set of reduced proper fractions for `d ≤ n`. The function should only consider fractions where the numerator and denominator are coprime. The function should use the Farey sequence algorithm to generate and check the fractions.
"""

def count_fractions(n):
    """
    Returns the number of fractions that lie between 1/2 and 2/3 in the sorted set of reduced proper fractions for d ≤ n.
    
    Args:
    n (int): The upper limit for the denominator.

    Returns:
    int: The number of fractions in the specified range.
    """
    a, b, c, d = 1, 2, 2, 3
    counter = 0
    while True:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        if a/b < 1/2:
            continue
        if 2/3 < a/b:
            break
        counter += 1
    return counter