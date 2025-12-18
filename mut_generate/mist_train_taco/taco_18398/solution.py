"""
QUESTION:
Help Johnny!
He can't make his code work!
Easy Code
Johnny is trying to make a function that adds the sum of two encoded strings, but he can't find the error in his code! Help him!
"""

def sum_encoded_strings(s1: str, s2: str) -> int:
    return sum((ord(x) for x in s1 + s2))