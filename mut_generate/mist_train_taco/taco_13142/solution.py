"""
QUESTION:
Given is a string S. Replace every character in S with x and print the result.

-----Constraints-----
 - S is a string consisting of lowercase English letters.
 - The length of S is between 1 and 100 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Replace every character in S with x and print the result.

-----Sample Input-----
sardine

-----Sample Output-----
xxxxxxx

Replacing every character in S with x results in xxxxxxx.
"""

def replace_with_x(S: str) -> str:
    """
    Replace every character in the input string S with 'x' and return the result.

    Parameters:
    S (str): A string consisting of lowercase English letters.

    Returns:
    str: A string where every character in S is replaced with 'x'.
    """
    return 'x' * len(S)