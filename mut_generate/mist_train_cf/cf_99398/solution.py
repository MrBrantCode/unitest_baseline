"""
QUESTION:
Write a Python function `pig_latin(phrase)` that converts a given phrase into Pig Latin. The function should handle both lowercase and capitalized words, maintaining the original capitalization in the output. It should use a dictionary to map vowels and consonants, and implement the standard Pig Latin rules: if the word starts with a vowel, add 'way' to the end; if it starts with a consonant, move the consonant to the end and add 'ay'.
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