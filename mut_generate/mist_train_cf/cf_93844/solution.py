"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string, and a constant space complexity. The solution should not use built-in string manipulation functions, external libraries, or modules, and should handle strings containing uppercase and lowercase letters, as well as special characters.
"""

def reverse_string(string):
    chars = list(string)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return "".join(chars)