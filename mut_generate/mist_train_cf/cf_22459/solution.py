"""
QUESTION:
Write a function `pig_latin_converter` that takes a string as input and returns its Pig Latin equivalent. The rules for converting to Pig Latin are as follows: 

- If a word starts with a consonant cluster, move the entire cluster to the end of the word and add "ay" at the end.
- If a word starts with a vowel or a vowel cluster, simply add "way" at the end.
"""

def pig_latin_converter(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + 'way')
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1
            pig_latin_words.append(word[i:] + word[:i] + 'ay')

    return ' '.join(pig_latin_words)