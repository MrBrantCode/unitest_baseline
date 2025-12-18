"""
QUESTION:
Write a function `are_scrambled_strings(s1, s2)` that takes two character sequence strings `s1` and `s2` as input and returns `True` if they are scrambled versions of each other, and `False` otherwise. The function should not use any pre-established library functionalities or data organization systems. The input strings are assumed to be in lowercase.
"""

def are_scrambled_strings(s1, s2):
    if len(s1) != len(s2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(s1)):
        count1[ord(s1[i]) - ord('a')] += 1 
        count2[ord(s2[i]) - ord('a')] += 1 

    return count1 == count2