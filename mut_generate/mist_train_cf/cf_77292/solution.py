"""
QUESTION:
Create a function named `common_chars_dict` that takes two strings as input, `str1` and `str2`, and returns a dictionary. The dictionary should have characters as keys and the minimum number of occurrences of each character in both strings as values. The comparison should be case-sensitive, meaning 'a' and 'A' are considered different characters. The function should only count the minimal number of common occurrences if a character appears multiple times in both strings.
"""

def common_chars_dict(str1, str2):
    common_chars = {}
    for char in set(str1):
        if char in str2:
            common_chars[char] = min(str1.count(char), str2.count(char))
    return common_chars