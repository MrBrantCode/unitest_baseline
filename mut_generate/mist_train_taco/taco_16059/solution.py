"""
QUESTION:
The door of Snuke's laboratory is locked with a security code.
The security code is a 4-digit number. We say the security code is hard to enter when it contains two consecutive digits that are the same.
You are given the current security code S. If S is hard to enter, print Bad; otherwise, print Good.

-----Constraints-----
 - S is a 4-character string consisting of digits.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
If S is hard to enter, print Bad; otherwise, print Good.

-----Sample Input-----
3776

-----Sample Output-----
Bad

The second and third digits are the same, so 3776 is hard to enter.
"""

def is_security_code_hard_to_enter(S: str) -> str:
    """
    Determines if the given 4-digit security code is hard to enter.

    Args:
        S (str): A 4-character string consisting of digits.

    Returns:
        str: 'Bad' if the code contains two consecutive digits that are the same, otherwise 'Good'.
    """
    if any(S[i] == S[i + 1] for i in range(3)):
        return 'Bad'
    else:
        return 'Good'