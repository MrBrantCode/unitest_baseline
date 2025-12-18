"""
QUESTION:
Write a function called `remove_duplicates` that takes a string `s` as input and returns a tuple containing the string with duplicate characters removed and the number of duplicates removed. The function should maintain the original order of non-duplicated characters. The input string only contains lowercase English letters. The function should run in linear time complexity O(n) where n is the length of the input string.
"""

def remove_duplicates(s):
    char_count = {}
    result = ''
    num_duplicates = 0

    for char in s:
        if char not in char_count:
            char_count[char] = 1
            result += char
        else:
            char_count[char] += 1
            num_duplicates += 1

    return result, num_duplicates