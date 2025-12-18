"""
QUESTION:
Create a function called `extract_characters` that takes an input string and returns a new string containing all characters from the input string. Do not use built-in string manipulation functions or methods, including for loops or recursion. The solution should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def extract_characters(input_string):
    input_list = list(input_string)
    return "".join(input_list)