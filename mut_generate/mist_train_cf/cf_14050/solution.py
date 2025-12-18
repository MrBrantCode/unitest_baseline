"""
QUESTION:
Write a function `compare_strings` that compares two input strings `str1` and `str2` and returns the number of different characters between them. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the longer string.
"""

def compare_strings(str1, str2):
    length = max(len(str1), len(str2))
    count = 0
    for i in range(length):
        if i >= len(str1) or i >= len(str2) or str1[i] != str2[i]:
            count += 1
    return count