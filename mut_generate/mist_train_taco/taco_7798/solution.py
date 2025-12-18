"""
QUESTION:
Given is a three-digit integer N. Does N contain the digit 7?
If so, print Yes; otherwise, print No.

-----Constraints-----
 - 100 \leq N \leq 999

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If N contains the digit 7, print Yes; otherwise, print No.

-----Sample Input-----
117

-----Sample Output-----
Yes

117 contains 7 as its last digit.
"""

def contains_digit_seven(N: int) -> str:
    """
    Determines if the given three-digit integer N contains the digit 7.

    Parameters:
    - N (int): A three-digit integer (100 <= N <= 999).

    Returns:
    - str: "Yes" if N contains the digit 7, otherwise "No".
    """
    return 'Yes' if '7' in str(N) else 'No'