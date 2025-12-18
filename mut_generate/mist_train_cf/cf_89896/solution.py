"""
QUESTION:
Write a function `find_mismatched_index` that compares two strings `str1` and `str2`, both consisting of only lowercase letters without repeating characters, with `str1` having a maximum length of 20 characters and `str2` having a maximum length of 30 characters. The function should return the index of the first mismatched character where the ASCII value difference is at least 10. If no such mismatch is found, return the length of the shorter string. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the shorter string.
"""

def find_mismatched_index(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i] and abs(ord(str2[i]) - ord(str1[i])) >= 10:
            return i
    return min_length