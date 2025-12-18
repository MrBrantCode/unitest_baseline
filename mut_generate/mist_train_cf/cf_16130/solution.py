"""
QUESTION:
Write a function `find_subsequence_index(string, integer)` that finds the index of the first occurrence of a specific subsequence of characters in the string. The subsequence consists of the digits in the integer concatenated in ascending order. If the subsequence is not found, return -1. The function should have a time complexity of O(n), where n is the length of the string.
"""

def find_subsequence_index(string, integer):
    subsequence = ''.join(sorted(str(integer)))
    subsequence_index = 0
    for i in range(len(string)):
        if string[i] == subsequence[subsequence_index]:
            subsequence_index += 1
            if subsequence_index == len(subsequence):
                return i - subsequence_index + 1
    return -1