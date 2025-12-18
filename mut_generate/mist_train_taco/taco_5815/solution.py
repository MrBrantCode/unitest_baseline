"""
QUESTION:
An uppercase or lowercase English letter \alpha will be given as input.
If \alpha is uppercase, print A; if it is lowercase, print a.

-----Constraints-----
 - \alpha is an uppercase (A - Z) or lowercase (a - z) English letter.

-----Input-----
Input is given from Standard Input in the following format:
α

-----Output-----
If \alpha is uppercase, print A; if it is lowercase, print a.

-----Sample Input-----
B

-----Sample Output-----
A

B is uppercase, so we should print A.
"""

def determine_case(alpha: str) -> str:
    """
    Determines the case of the input letter and returns 'A' if it is uppercase, 'a' if it is lowercase.

    Parameters:
    alpha (str): A single character string representing the input letter.

    Returns:
    str: 'A' if alpha is uppercase, 'a' if alpha is lowercase.
    """
    if alpha.isupper():
        return 'A'
    else:
        return 'a'