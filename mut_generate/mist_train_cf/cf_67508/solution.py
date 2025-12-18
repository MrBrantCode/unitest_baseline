"""
QUESTION:
Implement a function `translate_to_pig_latin(sentence)` that translates a given English sentence into Pig Latin. The function should split the sentence into words and translate each word according to the basic Pig Latin rules: if the word starts with a vowel, append 'way' to the end, and if it starts with a consonant, move the first letter to the end and append 'ay'. The function should return the translated sentence.
"""

def translate_to_pig_latin(sentence):
    words = sentence.split()
    translated_words = []
    for word in words:
        if word[0] in 'aeiou':
            translated_words.append(word + 'way')
        else:
            translated_words.append(word[1:] + word[0] + 'ay')

    return ' '.join(translated_words)