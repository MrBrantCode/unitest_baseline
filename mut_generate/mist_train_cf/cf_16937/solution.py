"""
QUESTION:
Write a function `sentence_reverse(sentence)` that takes a string as input, reverses the order of words in the sentence while preserving special characters and punctuation, and returns the result as a string. The function should handle leading and trailing whitespaces in the input sentence by removing them.
"""

def sentence_reverse(sentence):
    sentence = sentence.strip()
    words = sentence.split()
    words = words[::-1]
    reversed_sentence = ' '.join(words)
    return reversed_sentence