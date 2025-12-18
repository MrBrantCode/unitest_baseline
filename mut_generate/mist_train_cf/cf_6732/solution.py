"""
QUESTION:
Write a function named "reverse_sentence" that takes a string as input, reverses each word individually while preserving the punctuation and capitalization, and returns the modified string with the original order of words and spacing intact.
"""

def reverse_sentence(sentence):
    words = sentence.split(" ")
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence