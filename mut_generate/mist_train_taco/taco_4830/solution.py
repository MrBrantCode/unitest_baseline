"""
QUESTION:
Compute A \times B, truncate its fractional part, and print the result as an integer.

-----Constraints-----
 - 0 \leq A \leq 10^{15}
 - 0 \leq B < 10
 - A is an integer.
 - B is a number with two digits after the decimal point.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the answer as an integer.

-----Sample Input-----
198 1.10

-----Sample Output-----
217

We have 198 \times 1.10 = 217.8. After truncating the fractional part, we have the answer: 217.
"""

from decimal import Decimal

def compute_truncated_product(A: int, B: str) -> int:
    """
    Computes the product of A and B, truncates its fractional part, and returns the result as an integer.

    Parameters:
    - A (int): The first number, an integer between 0 and 10^15.
    - B (str): The second number, a string representing a number with two digits after the decimal point.

    Returns:
    - int: The truncated product of A and B.
    """
    return int(Decimal(A) * Decimal(B))