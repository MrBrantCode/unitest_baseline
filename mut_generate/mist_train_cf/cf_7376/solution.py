"""
QUESTION:
Write a function `find_mismatched_index` that compares two lowercase strings, `str1` and `str2`, and returns the index of the first mismatched character. The function should only consider strings where `str1` has a maximum length of 20 characters and `str2` has a maximum length of 30 characters, and both strings consist of unique characters. The mismatched characters should have a minimum ASCII value difference of 10. If no mismatch is found, return the length of the shorter string. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_mismatched_index(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i] and abs(ord(str2[i]) - ord(str1[i])) >= 10:
            return i
    return min_length