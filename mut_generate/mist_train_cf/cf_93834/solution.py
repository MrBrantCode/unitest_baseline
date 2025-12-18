"""
QUESTION:
Write a function `remove_vowels(string)` that takes a string as input and returns a new string with all vowels removed. The function should have a time complexity of O(n), where n is the length of the input string, and use constant space complexity, handling both uppercase and lowercase vowels.
"""

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string