"""
QUESTION:
AtCoDeer the deer found two positive integers, a and b.
Determine whether the product of a and b is even or odd.

-----Constraints-----
 - 1 ≤ a,b ≤ 10000
 - a and b are integers.

-----Input-----
Input is given from Standard Input in the following format:
a b

-----Output-----
If the product is odd, print Odd; if it is even, print Even.

-----Sample Input-----
3 4

-----Sample Output-----
Even

As 3 × 4 = 12 is even, print Even.
"""

def determine_product_parity(a: int, b: int) -> str:
    """
    Determines whether the product of two integers a and b is odd or even.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    str: "Odd" if the product is odd, "Even" if the product is even.
    """
    product = a * b
    return 'Odd' if product % 2 != 0 else 'Even'