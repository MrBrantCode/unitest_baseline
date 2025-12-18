"""
QUESTION:
Implement a function `isNice(string)` that takes a string as input and returns `True` if the string contains at least one pair of two letters that appears at least twice in the string without overlapping, and it also contains at least one letter which repeats with exactly one letter between them.
"""

def isNice(string):
    pair_found = False
    repeat_with_gap_found = False

    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if string.count(pair) >= 2:
            pair_found = True
            break

    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            repeat_with_gap_found = True
            break

    return pair_found and repeat_with_gap_found