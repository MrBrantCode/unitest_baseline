"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a string `sentence` as input, reverses the order of the words in the sentence, and returns the modified string while keeping the order of characters in each word unchanged. The function should split the sentence into words, reverse their order, and then join them back into a string with spaces in between.
"""

def reverse_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence