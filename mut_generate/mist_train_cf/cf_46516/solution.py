"""
QUESTION:
Write a function named `count_ab` that takes a string `s` as input and returns the number of 'ab' substrings in the string, preserving the order. The function should not use any built-in functions. The string `s` may contain characters other than 'a' and 'b'. The function should avoid any potential index out of range errors.
"""

def count_ab(s):
    count = 0
    previous = None
    for char in s:
        if char == 'b' and previous == 'a':
            count += 1
        previous = char
    return count