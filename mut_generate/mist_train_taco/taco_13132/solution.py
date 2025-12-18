"""
QUESTION:
Given is an integer x that is greater than or equal to 0, and less than or equal to 1.
Output 1 if x is equal to 0, or 0 if x is equal to 1.

-----Constraints-----
 - 0 \leq x \leq 1
 - x is an integer

-----Input-----
Input is given from Standard Input in the following format:
x

-----Output-----
Print 1 if x is equal to 0, or 0 if x is equal to 1.

-----Sample Input-----
1

-----Sample Output-----
0
"""

def convert_x_to_output(x: int) -> int:
    """
    Converts the input integer x to an output based on the given conditions.

    Parameters:
    x (int): An integer that is greater than or equal to 0 and less than or equal to 1.

    Returns:
    int: 1 if x is 0, or 0 if x is 1.
    """
    return 1 - x