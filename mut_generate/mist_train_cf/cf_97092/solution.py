"""
QUESTION:
Write a function `pig_latin_converter` that takes a string as input and returns its Pig Latin equivalent. The conversion rules are as follows:
- If a word starts with a consonant cluster, move the entire cluster to the end of the word and add "ay".
- If a word starts with a vowel or a vowel cluster, add "way" at the end.
Assume that the input string is a sentence with multiple words separated by spaces and that the sentence only contains letters.
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