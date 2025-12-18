"""
QUESTION:
Write a function `process_string(input_string)` that takes a string of lowercase letters and spaces as input, removes all vowels, reverses the characters, and replaces all spaces with '*'. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in functions or data structures.
"""

def process_string(input_string):
    result = ""
    for i in range(len(input_string) - 1, -1, -1):
        c = input_string[i]
        if c not in ['a', 'e', 'i', 'o', 'u']:
            if c != ' ':
                result += c
            else:
                result += '*'
    return result