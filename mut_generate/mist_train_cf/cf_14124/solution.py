"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input, reverses it without using any additional data structures, and returns the reversed string. The function should have a time complexity of O(n) and a space complexity of O(1). Note that the input string is immutable, so it may need to be converted to a mutable data structure before reversing.
"""

def reverse_string(s):
    s = list(s)
    start = 0
    end = len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)