"""
QUESTION:
Implement a function `pig_latin_converter` that takes a string as input and returns its Pig Latin equivalent. The function should follow these rules: 
- if the input string starts with a vowel ('a', 'e', 'i', 'o', 'u'), append 'way' to the end of the string.
- if the input string starts with a consonant, move the consonant to the end of the string and append 'ay'.
"""

def pig_latin_converter(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'