"""
QUESTION:
Given a number n. Find the last two digits of 5 ^ n ( 5 to the power of n ).
Remember that overflow can occur.

-----Input:-----
- N  — the power in which you need to raise number 5.

-----Output:-----
Last two digits of 5^n.

-----Constraints-----
- $2 \leq N \leq 2.1018$

-----Sample Input:-----
2

-----Sample Output:-----
25
"""

def last_two_digits_of_power_of_five(n: int) -> int:
    """
    Calculate the last two digits of 5^n.

    Parameters:
    n (int): The power to which the number 5 is raised.

    Returns:
    int: The last two digits of 5^n.
    """
    if n == 0:
        return 1  # Special case: 5^0 = 1
    elif n == 1:
        return 5  # Special case: 5^1 = 5
    else:
        return 25  # For n >= 2, the last two digits of 5^n are always 25