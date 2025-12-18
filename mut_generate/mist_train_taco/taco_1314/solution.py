"""
QUESTION:
Given are two strings S and T consisting of lowercase English letters. Concatenate T and S in this order, without space in between, and print the resulting string.

-----Constraints-----
 - S and T are strings consisting of lowercase English letters.
 - The lengths of S and T are between 1 and 100 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
S T

-----Output-----
Print the resulting string.

-----Sample Input-----
oder atc

-----Sample Output-----
atcoder

When S =  oder and T =  atc, concatenating T and S in this order results in atcoder.
"""

def concatenate_strings(S: str, T: str) -> str:
    """
    Concatenates the string T followed by the string S and returns the resulting string.

    Parameters:
    S (str): A string consisting of lowercase English letters.
    T (str): A string consisting of lowercase English letters.

    Returns:
    str: The concatenated string of T followed by S.
    """
    return T + S