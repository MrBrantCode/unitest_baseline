"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and reverses it in place without using any additional data structures. The function should have a time complexity of O(n) and a space complexity of O(1).
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