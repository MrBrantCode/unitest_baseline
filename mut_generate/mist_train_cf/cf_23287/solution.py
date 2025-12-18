"""
QUESTION:
Write a function `pig_latin(sentence)` that takes a sentence as input and returns the sentence translated into Pig Latin. The rules for Pig Latin are as follows: if a word begins with a vowel, append 'ay' to the end of the word; if a word begins with a consonant, move the consonant to the end of the word and append 'ay'. The function should work for sentences with multiple words.
"""

def pig_latin(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if word[0].lower() in 'aeiou':
            new_words.append(word + 'ay')
        else:
            new_words.append(word[1:] + word[0] + 'ay')
    return ' '.join(new_words)