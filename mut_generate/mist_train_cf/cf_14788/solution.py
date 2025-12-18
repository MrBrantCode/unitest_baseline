"""
QUESTION:
Create a function named `remove_vowels_reverse` that takes a string as input and returns the resulting string with all vowels removed and in reverse order.
"""

def remove_vowels_reverse(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result[::-1]