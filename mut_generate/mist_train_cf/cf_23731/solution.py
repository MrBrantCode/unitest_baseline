"""
QUESTION:
Write a function called `longest_substring` that takes a string as input and returns the length of the longest substring without repeating characters. The function should be able to handle strings with any characters and should have a time complexity of O(n), where n is the length of the string.
"""

def longest_substring(s):
    start = 0
    max_length = 0
    used_char = {}

    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_char[char] = i

    return max_length