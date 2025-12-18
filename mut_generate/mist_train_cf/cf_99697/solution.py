"""
QUESTION:
Write a function named `reverse_sentence(sentence)` that takes a string input `sentence`, reverses the order of its words, and returns the resulting string. The function should be able to handle sentences with any number of words, and the words should be separated by spaces in the output string.
"""

def reverse_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_sentence = " ".join(reversed_words)  # Join the words into a sentence
    return reversed_sentence