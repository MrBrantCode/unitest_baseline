"""
QUESTION:
Write a function named `count_unique_chars` that takes a string as input and returns the number of unique characters in the string. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. You are not allowed to use any built-in functions or libraries for counting or manipulating characters, such as `collections.Counter` or `set()`. The input string only contains ASCII characters.
"""

def count_unique_chars(string):
    unique_chars = 0
    char_count = [0] * 128

    for char in string:
        char_code = ord(char)
        if char_count[char_code] == 0:
            unique_chars += 1
            char_count[char_code] = 1

    return unique_chars