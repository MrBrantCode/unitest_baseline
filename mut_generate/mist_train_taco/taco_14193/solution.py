"""
QUESTION:
You are given two integers A and B.
Find the largest value among A+B, A-B and A \times B.

-----Constraints-----
 - -1000 \leq A,B \leq 1000
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the largest value among A+B, A-B and A \times B.

-----Sample Input-----
3 1

-----Sample Output-----
4

3+1=4, 3-1=2 and 3 \times 1=3. The largest among them is 4.
"""

def find_largest_value(A: int, B: int) -> int:
    """
    Find the largest value among A + B, A - B, and A * B.

    Parameters:
    - A (int): The first integer input.
    - B (int): The second integer input.

    Returns:
    - int: The largest value among A + B, A - B, and A * B.
    """
    return max(A + B, A - B, A * B)