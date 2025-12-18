"""
QUESTION:
Create a function `first_uniq_char(s)` that finds the index of the first unique character in a given string `s`. If the string contains all repetitive characters or is empty, return -1. The function should consider special characters as well.
"""

def first_uniq_char(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1