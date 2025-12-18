"""
QUESTION:
You are given a string S of length 3 consisting of a, b and c. Determine if S can be obtained by permuting abc.

-----Constraints-----
 - |S|=3
 - S consists of a, b and c.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
If S can be obtained by permuting abc, print Yes; otherwise, print No.

-----Sample Input-----
bac

-----Sample Output-----
Yes

Swapping the first and second characters in bac results in abc.
"""

def can_form_abc(S: str) -> str:
    """
    Determines if the given string S of length 3 can be obtained by permuting 'abc'.

    Parameters:
    S (str): A string of length 3 consisting of characters 'a', 'b', and 'c'.

    Returns:
    str: 'Yes' if S can be obtained by permuting 'abc', otherwise 'No'.
    """
    return 'Yes' if set(S) == {'a', 'b', 'c'} else 'No'