"""
QUESTION:
Write a function called `break_string` that takes a string as input and returns a tuple of three strings. The first string in the tuple should contain all the consonants from the input string, the second string should contain all the vowels, and the third string should contain any other characters. The function should handle both uppercase and lowercase characters and should preserve the original case of the characters in the input string.
"""

def break_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(97, 123) if chr(i) not in vowels]
    consonants += [chr(i).upper() for i in range(97, 123) if chr(i).upper() not in vowels]

    consonant_str = ''
    vowel_str = ''
    other_str = ''

    for char in string:
        if char.lower() in vowels:
            vowel_str += char
        elif char.lower() in consonants:
            consonant_str += char
        else:
            other_str += char

    return consonant_str, vowel_str, other_str