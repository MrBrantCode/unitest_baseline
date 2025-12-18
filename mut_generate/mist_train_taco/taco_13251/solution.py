"""
QUESTION:
Given a lowercase English letter c, determine whether it is a vowel. Here, there are five vowels in the English alphabet: a, e, i, o and u.

-----Constraints-----
 - c is a lowercase English letter.

-----Input-----
The input is given from Standard Input in the following format:
c

-----Output-----
If c is a vowel, print vowel. Otherwise, print consonant.

-----Sample Input-----
a

-----Sample Output-----
vowel

Since a is a vowel, print vowel.
"""

def is_vowel(c: str) -> str:
    """
    Determines whether the given lowercase English letter is a vowel.

    Parameters:
    c (str): A single lowercase English letter.

    Returns:
    str: 'vowel' if c is a vowel, otherwise 'consonant'.
    """
    vowels = 'aeiou'
    return 'vowel' if c in vowels else 'consonant'