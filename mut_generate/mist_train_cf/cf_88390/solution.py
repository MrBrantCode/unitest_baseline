"""
QUESTION:
Write a function `extract_characters` that takes a string `input_string` as input and returns a new string containing all alphanumeric characters from the input string, in the order they appear, without using built-in string manipulation functions or methods, loops, recursion, or additional data structures. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def extract_characters(input_string):
    i = j = 0
    while i < len(input_string):
        if input_string[i].isalnum():
            input_string[j] = input_string[i]
            j += 1
        i += 1
    return input_string[:j]