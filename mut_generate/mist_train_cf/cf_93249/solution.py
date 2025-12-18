"""
QUESTION:
Write a function `count_occurrences` that takes two strings `string1` and `string2` as input and returns the total number of non-overlapping occurrences of `string2` in `string1`. The function should handle cases where `string2` is an empty string, in which case it should return 0.
"""

def count_occurrences(string1, string2):
    if string2 == "":
        return 0
    else:
        count = 0
        i = 0
        while i < len(string1):
            if string1[i:i+len(string2)] == string2:
                count += 1
                i += len(string2)
            else:
                i += 1
        return count