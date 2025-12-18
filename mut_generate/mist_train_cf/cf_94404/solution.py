"""
QUESTION:
Write a function named `find_length` that calculates the length of a given null-terminated string without using any built-in functions or libraries that directly give the length of a string, loops, or recursion. The function should have a time complexity of less than O(n), where n is the length of the string.
"""

def find_length(s):
    low, high = 0, 1
    while True:
        try:
            _ = s[high]
            low = high
            high *= 2
        except IndexError:
            return low