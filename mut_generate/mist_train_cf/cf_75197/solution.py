"""
QUESTION:
Write a function named `remove_consonants` that takes a string `input_string` as input and returns a new string with all consonantal alphabetic characters removed. The function should consider both lowercase and uppercase vowels. Non-alphabetic characters in the string should be preserved in the output.
"""

def remove_consonants(input_string):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in input_string:
        if char in vowels or not char.isalpha():
            result += char
    return result