"""
QUESTION:
Write a Python function `is_isogram(string)` that determines if the input string is an isogram, a word or phrase with no repeating letters, disregarding non-alphabet characters and letter case. The function should return a boolean value.
"""

def is_isogram(string):
    # Remove any non-alphabet characters and convert to lower case
    clean_string = ''.join(filter(str.isalpha, string)).lower()
    
    # Compare the length of the set of letters to the length of the string
    return len(set(clean_string)) == len(clean_string)