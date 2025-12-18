"""
QUESTION:
Create a Python function `merge_strings` that takes two string inputs and returns their concatenation without using any built-in string concatenation functions. The function should handle varying character data types, including special symbols and non-English alphabetical characters, without generating any errors.
"""

def merge_strings(string1, string2):
    result = ''
    for i in string1:
        result += i
    for j in string2:
        result += j
    return result