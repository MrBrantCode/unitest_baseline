"""
QUESTION:
Create a function `greet(name)` that takes a string `name` as input, reverses the order of its consonants, and returns a string consisting of "Bonjour" followed by a space and the reversed consonants. The function should also include error handling to return an error message if the input is not a string.
"""

def greet(name):
    if type(name) != str:
        return "Error: Input must be a string."
        
    reversed_consonants = ''
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    for char in name:
        if char in consonants:
            reversed_consonants = char + reversed_consonants

    return 'Bonjour ' + reversed_consonants