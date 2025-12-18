"""
QUESTION:
Compute A \times B.

-----Constraints-----
 - 1 \leq A \leq 100
 - 1 \leq B \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the value A \times B as an integer.

-----Sample Input-----
2 5

-----Sample Output-----
10

We have 2 \times 5 = 10.
"""

def multiply_numbers(A: int, B: int) -> int:
    """
    Computes the product of two integers A and B.

    Parameters:
    - A (int): The first integer.
    - B (int): The second integer.

    Returns:
    - int: The product of A and B.
    """
    return A * B