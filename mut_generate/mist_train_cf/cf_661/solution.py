"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), meaning it should not use any additional memory other than the input string.
"""

def reverse_string(string):
    chars = list(string)
    length = len(chars)
    left = 0
    right = length - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)