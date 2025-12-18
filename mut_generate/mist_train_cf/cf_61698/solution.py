"""
QUESTION:
Write a function named `count_ab` that takes a string `s` as input and returns the number of 'ab' substrings in `s`. The function should not use in-built Python functions or regular expressions, and it should handle edge cases such as an empty string, a string with letters other than 'a' and 'b', and a string with no 'ab' substrings.
"""

def count_ab(s):
    count = 0
    for i in range(len(s) - 1):  
        if s[i] == 'a' and s[i+1] == 'b':  
            count += 1
    return count