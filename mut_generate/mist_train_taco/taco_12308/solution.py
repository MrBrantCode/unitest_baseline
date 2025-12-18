"""
QUESTION:
You are given three integers A, B and C.
Determine whether C is not less than A and not greater than B.

-----Constraints-----
 - -100≤A,B,C≤100 
 - A, B and C are all integers.

-----Input-----
Input is given from Standard Input in the following format:  
A B C

-----Output-----
If the condition is satisfied, print Yes; otherwise, print No.

-----Sample Input-----
1 3 2

-----Sample Output-----
Yes

C=2 is not less than A=1 and not greater than B=3, and thus the output should be Yes.
"""

def is_within_range(A: int, B: int, C: int) -> str:
    """
    Determines whether the integer C is within the range [A, B].

    Parameters:
    - A (int): The lower bound of the range.
    - B (int): The upper bound of the range.
    - C (int): The integer to be checked.

    Returns:
    - str: "Yes" if C is within the range [A, B], otherwise "No".
    """
    return "Yes" if A <= C <= B else "No"