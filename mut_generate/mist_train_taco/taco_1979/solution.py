"""
QUESTION:
Given an integer a as input, print the value a + a^2 + a^3.

-----Constraints-----
 - 1 \leq a \leq 10
 - a is an integer.

-----Input-----
Input is given from Standard Input in the following format:
a

-----Output-----
Print the value a + a^2 + a^3 as an integer.

-----Sample Input-----
2

-----Sample Output-----
14

When a = 2, we have a + a^2 + a^3 = 2 + 2^2 + 2^3 = 2 + 4 + 8 = 14.
Print the answer as an input. Outputs such as 14.0 will be judged as incorrect.
"""

def calculate_polynomial_sum(a: int) -> int:
    """
    Calculate the sum of a polynomial expression a + a^2 + a^3.

    Parameters:
    a (int): An integer in the range [1, 10].

    Returns:
    int: The result of the polynomial expression a + a^2 + a^3.
    """
    return a + a**2 + a**3