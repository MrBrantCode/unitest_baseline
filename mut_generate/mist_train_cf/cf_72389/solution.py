"""
QUESTION:
Write a function called `pig_latin_converter` that takes a string `text` as input. This function should first remove all punctuation from the input string, then convert each word in the string to Pig Latin. The conversion to Pig Latin should be done according to the following rules: if a word starts with a vowel, add 'ay' to the end; if a word starts with a consonant, move the consonant to the end and add 'ay'. Return the resulting string. Assume all input strings are in English and only contain letters and punctuation.
"""

def pig_latin_converter(text):
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    text_list = text.lower().split() 
    vowels = ['a', 'e', 'i', 'o', 'u']
    piglatin = []

    for word in text_list:
        first = word[0]
        if first in vowels:  # word starts with a vowel
            piglatin.append(word + 'ay')
        else:  # word starts with a consonant 
            piglatin.append(word[1:] + first + 'ay')
    return ' '.join(piglatin)