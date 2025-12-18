"""
QUESTION:
You are given nonnegative integers a and b (a ≤ b), and a positive integer x.
Among the integers between a and b, inclusive, how many are divisible by x?

-----Constraints-----
 - 0 ≤ a ≤ b ≤ 10^{18}
 - 1 ≤ x ≤ 10^{18}

-----Input-----
The input is given from Standard Input in the following format:
a b x

-----Output-----
Print the number of the integers between a and b, inclusive, that are divisible by x.

-----Sample Input-----
4 8 2

-----Sample Output-----
3

There are three integers between 4 and 8, inclusive, that are divisible by 2: 4, 6 and 8.
"""

def count_divisibles_in_range(a: int, b: int, x: int) -> int:
    """
    Counts the number of integers between `a` and `b` (inclusive) that are divisible by `x`.

    Parameters:
    - a (int): The lower bound of the range (inclusive).
    - b (int): The upper bound of the range (inclusive).
    - x (int): The divisor to check for divisibility.

    Returns:
    - int: The number of integers between `a` and `b` that are divisible by `x`.
    """
    return b // x - (a - 1) // x