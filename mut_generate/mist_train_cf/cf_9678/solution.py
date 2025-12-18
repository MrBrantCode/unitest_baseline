"""
QUESTION:
Write a function called `find_subsequence_index` that takes a string and an integer as input and returns the index of the first occurrence of a specific subsequence of characters in the string. The subsequence consists of the digits in the integer concatenated in ascending order. If the subsequence is not found, return -1.
"""

def find_subsequence_index(string, integer):
    subsequence = ''.join(sorted(str(integer)))
    index = string.find(subsequence)
    return index