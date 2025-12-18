"""
QUESTION:
Write a Python function `pig_latin(phrase)` that takes a string phrase as input, converts it into Pig Latin, and returns the result. The function should handle both lowercase and uppercase letters, preserving the original capitalization of each word.
"""

def pig_latin(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    pig_latin_phrase = []
    for word in phrase.split():
        if word[0].isupper():
            is_capitalized = True
            word = word.lower()
        else:
            is_capitalized = False
        if word[0] in vowels:
            pig_latin_word = word + 'way'
        else:
            pig_latin_word = word[1:] + word[0] + 'ay'
        if is_capitalized:
            pig_latin_word = pig_latin_word.capitalize()
        pig_latin_phrase.append(pig_latin_word)
    return ' '.join(pig_latin_phrase)