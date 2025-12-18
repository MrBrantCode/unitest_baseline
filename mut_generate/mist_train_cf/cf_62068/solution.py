"""
QUESTION:
Implement a function named `condense_string` that takes a string `s` as input and returns a new string where each unique character in `s` is followed by its count. For example, if `s` is "aaabbbccc", the output should be "a3b3c3". The function should have a time complexity of O(n), where n is the length of the string `s`.
"""

def condense_string(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return ''.join(f'{char}{count}' for char, count in char_count.items())