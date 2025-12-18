"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in library functions or additional data structures. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)