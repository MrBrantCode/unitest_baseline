"""
QUESTION:
Implement a function `extract_characters` that takes an input string as a list of characters and returns a new string containing all alphanumeric characters from the input string. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string. It should not use any built-in string manipulation functions or methods, loops, or recursion. It should manipulate the characters directly within the input string itself.
"""

def extract_characters(input_string):
    i = j = 0
    while input_string[i] != '\0':
        if input_string[i].isalnum():
            input_string[j] = input_string[i]
            j += 1
        i += 1
    input_string[j] = '\0'
    return input_string[:j]