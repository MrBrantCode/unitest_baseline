"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and reverses the order of its characters. The function should not use any built-in string manipulation functions or libraries, and it should only use a loop or iteration. Additionally, the function should not create any new variables or data structures and should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    length = len(s)
    start = 0
    end = length - 1

    while start < end:
        s = list(s)
        s[start], s[end] = s[end], s[start]
        s = ''.join(s)
        start += 1
        end -= 1

    return s