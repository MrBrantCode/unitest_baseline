"""
QUESTION:
Write a function `reverse_consonant_number(s)` that takes a string `s` as input and returns a new string where the order of consonants and numbers is reversed, while keeping vowels and special characters in their original positions. The function should preserve the case of consonants (uppercase or lowercase) and the value of numbers.
"""

def reverse_consonant_number(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonants += consonants.upper()
    numbers = "0123456789"
    
    stack = [ch for ch in s if ch in consonants or ch in numbers]
    output = ""
    for ch in s:
        if ch in consonants or ch in numbers:
            output += stack.pop()
        else:
            output += ch
    return output