"""
QUESTION:
Create a function named `compare_strings` that takes two parameters, `str1` and `str2`. The function should compare these two strings character by character and return a list of index positions where the characters differ. The comparison should be case-sensitive and able to handle strings of different lengths, comparing only up to the length of the shorter string and considering any remaining characters in the longer string as differing.
"""

def compare_strings(str1, str2):
    min_len = min(len(str1), len(str2))
    diffs = [i for i in range(min_len) if str1[i] != str2[i]]
    
    if len(str1) > len(str2):
        diffs += list(range(min_len, len(str1)))
    elif len(str2) > len(str1):
        diffs += list(range(min_len, len(str2)))

    return diffs