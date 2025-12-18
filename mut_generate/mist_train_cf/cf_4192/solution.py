"""
QUESTION:
Write a function named `process_string` that takes a string of lowercase letters and spaces as input. The function should return a new string where all vowels are removed, the remaining characters are in reverse order, and all spaces are replaced with '*'. The solution must have a time complexity of O(n), where n is the length of the input string, and cannot use any built-in functions or data structures.
"""

def process_string(input_string):
    result = ""
    for i in range(len(input_string) - 1, -1, -1):
        c = input_string[i]
        if c not in ['a', 'e', 'i', 'o', 'u']:
            result += c
    result = result[::-1]
    result = result.replace(' ', '*')
    return result