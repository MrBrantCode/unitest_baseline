"""
QUESTION:
Create a function `reverse_string_without_vowels` that takes a string as input and returns a new string that is the reverse of the original string, excluding any vowels (both uppercase and lowercase).
"""

def reverse_string_without_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    reversed_string = ""
    
    for char in s[::-1]:
        if char not in vowels:
            reversed_string += char
    
    return reversed_string