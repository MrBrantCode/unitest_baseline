"""
QUESTION:
Create a function `purge_vowels` that takes a string as input and returns the string with all vowels (both lowercase and uppercase) removed.
"""

def purge_vowels(input_string):
    vowels = 'aeiouAEIOU'
    for v in vowels:
        input_string = input_string.replace(v, '')
    return input_string