"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the string reversed, with every second character (starting from the second character) converted to its ASCII value. The function should not use any external libraries or built-in string reversal functions other than slicing.
"""

def reverse_string(s):
    reversed_string = s[::-1]  # Reverse the string
    result = ""
    for i in range(len(reversed_string)):
        # For every second character (from reversed string), get ASCII value
        if i % 2 != 0:
            result += str(ord(reversed_string[i]))
        else:
            result += reversed_string[i]
    return result