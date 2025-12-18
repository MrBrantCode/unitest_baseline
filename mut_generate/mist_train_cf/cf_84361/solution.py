"""
QUESTION:
Write a function `swap_case_and_replace_vowels` that takes a string as input, swaps the case of its letters, and replaces all vowels with asterisks (*). The function should handle non-alphabetic characters and return the modified string.
"""

def swap_case_and_replace_vowels(input_string):
    result = ""
    for char in input_string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                result += '*'
            elif char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    return result