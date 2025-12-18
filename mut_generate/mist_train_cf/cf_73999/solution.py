"""
QUESTION:
Write a function `sentence_to_pig_latin(sentence)` that takes a string as input and returns a string where punctuation has been removed and the sentence has been translated into Pig Latin according to the following rules: if a word starts with a vowel, 'way' is added to the end; if a word starts with a consonant, the consonant is moved to the end and 'ay' is added.
"""

def sentence_to_pig_latin(sentence):
    # Remove punctuation
    punctuation = '!()-[]{};:\'"\,<>./?@#$%^&*_~'
    for element in sentence: 
        if element in punctuation: 
            sentence = sentence.replace(element, "")

    # Convert sentence to Pig Latin
    words = sentence.split()
    for i in range(len(words)):
        word = words[i]
        first_letter = word[0]
        if first_letter.lower() in 'aeiou':
            word += 'way'
        else:
            word = word[1:] + first_letter + 'ay'
        words[i] = word
    return ' '.join(words)