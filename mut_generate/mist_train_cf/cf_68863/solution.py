"""
QUESTION:
Design a function `count_combinations(n, r)` that calculates the number of ways to choose `r` items from a set of size `n` without regard to the order of selection. The function should take two positive integers `n` and `r` as input and return the number of combinations. If `r` is greater than `n`, the function should return 0.
"""

def count_combinations(n, r):
    """
    Calculate the number of ways to choose r items from a set of size n without regard to the order of selection.

    Args:
        n (int): The size of the set.
        r (int): The number of items to be chosen.

    Returns:
        int: The number of combinations.
    """

    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            return fact

    if r > n:
        return 0
    else:
        return factorial(n) / (factorial(r) * factorial(n - r))