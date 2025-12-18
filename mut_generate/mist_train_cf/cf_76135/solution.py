"""
QUESTION:
Create a function `invert_positions(input_str)` that takes an input string and swaps the positions of each pair of adjacent characters if one is a vowel and the other is a consonant, while retaining the original positions of all other characters. The function should consider both lowercase and uppercase vowels and consonants.
"""

def invert_positions(input_str):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels += vowels.upper()
    consonants += consonants.upper()

    new_str = list(input_str)
    for i in range(len(input_str)-1):
        if (input_str[i] in vowels and input_str[i+1] in consonants) or \
           (input_str[i] in consonants and input_str[i+1] in vowels):
            new_str[i], new_str[i+1] = new_str[i+1], new_str[i]

    return ''.join(new_str)