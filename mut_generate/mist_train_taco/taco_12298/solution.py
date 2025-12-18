"""
QUESTION:
You are given two positive integers a and b.
Let x be the average of a and b.
Print x rounded up to the nearest integer.

-----Constraints-----
 - a and b are integers.
 - 1 \leq a, b \leq 100

-----Input-----
Input is given from Standard Input in the following format:
a b

-----Output-----
Print x rounded up to the nearest integer.

-----Sample Input-----
1 3

-----Sample Output-----
2

The average of 1 and 3 is 2.0, and it will be rounded up to the nearest integer, 2.
"""

def calculate_rounded_up_average(a: int, b: int) -> int:
    """
    Calculate the average of two integers a and b, and return the result rounded up to the nearest integer.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The average of a and b rounded up to the nearest integer.
    """
    return (a + b + 1) // 2