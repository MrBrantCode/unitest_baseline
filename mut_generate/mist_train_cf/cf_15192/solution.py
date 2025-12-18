"""
QUESTION:
Create a function called `pig_latin_converter` that takes a string as input and returns the string converted to Pig Latin. The function should handle punctuation marks by preserving their original positions, maintain the original capitalization of words, and only convert words with 10 characters or less.
"""

def pig_latin_converter(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if len(word) > 10:
            pig_latin_words.append(word)
            continue

        punctuation = ''
        if not word[-1].isalpha():
            punctuation = word[-1]
            word = word[:-1]

        capitalized = False
        if word[0].isupper():
            capitalized = True
            word = word.lower()

        if word[0] in vowels:
            pig_latin_word = word + 'way'
        else:
            pig_latin_word = word[1:] + word[0] + 'ay'

        if capitalized:
            pig_latin_word = pig_latin_word.capitalize()

        pig_latin_word += punctuation
        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)