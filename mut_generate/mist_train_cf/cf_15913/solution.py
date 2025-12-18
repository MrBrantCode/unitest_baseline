"""
QUESTION:
Write a function `find_differences` that takes two strings, `string1` and `string2`, as input and returns a list of tuples. Each tuple contains the index and the character where the strings differ, considering differences in letter casing. The output should be sorted in ascending order based on the index. The length of the input strings will be at most 10^6.
"""

def find_differences(string1, string2):
    result = []
    for i, (c1, c2) in enumerate(zip(string1, string2)):
        if c1.lower() != c2.lower():
            result.append((i, c2))
    return sorted(result, key=lambda x: x[0])