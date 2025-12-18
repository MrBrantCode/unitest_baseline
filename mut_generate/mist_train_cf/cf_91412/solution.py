"""
QUESTION:
Create a function called `reverse_string_without_vowels` that takes an input string `original_string` containing both uppercase and lowercase letters and returns a new string that is the reverse of the original string, excluding any vowels.
"""

def reverse_string_without_vowels(original_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    reversed_string = ""
    
    for char in original_string[::-1]:
        if char not in vowels:
            reversed_string += char
    
    return reversed_string