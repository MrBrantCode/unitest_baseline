"""
QUESTION:
Implement a function `pig_latin(phrase)` that converts a given phrase into Pig Latin, handling cases where the first letter of a word is capitalized and preserving the original capitalization in the output. The function should use a dictionary or list to map vowels and consonants, and move the first consonant (or consonant cluster) to the end of the word and append 'ay' to form the Pig Latin version, or simply append 'way' if the word starts with a vowel.
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