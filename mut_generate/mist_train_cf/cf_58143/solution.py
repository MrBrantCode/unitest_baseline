"""
QUESTION:
Write a function called `longest_unique_substring` that takes a string of alphanumeric characters as input and returns the longest continuous substring with the maximum number of unique characters. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(min(n,m)), where m is the size of the character set.
"""

def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_str = ""
    char_dict = {}

    for end, char in enumerate(s):
        if char in char_dict:
            start = max(start, char_dict[char] + 1)
        char_dict[char] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_str = s[start:end + 1]

    return max_str