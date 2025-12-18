"""
QUESTION:
Create a function named `mirror_words(sentence)` that takes a string `sentence` as input and returns a new string where each word in the input sentence is reversed. The original word order should be preserved, and the words should be separated by spaces.
"""

def mirror_words(sentence):
    # split the sentence into words
    words = sentence.split(' ')
    
    # mirror each word
    mirrored_words = [word[::-1] for word in words]
    
    # join the mirrored words into a sentence
    mirrored_sentence = ' '.join(mirrored_words)
    
    return mirrored_sentence