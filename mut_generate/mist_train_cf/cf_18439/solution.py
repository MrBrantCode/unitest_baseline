"""
QUESTION:
Create a function named `reverse_sentence(sentence)` that takes a sentence as input, reverses the order of words, reverses each word within itself, removes any duplicate words, and returns the resulting string. The function should run in O(n) time complexity, where n is the length of the sentence.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    reversed_words = [word[::-1] for word in reversed_sentence.split()]
    unique_words = list(dict.fromkeys(reversed_words))
    return ' '.join(unique_words)