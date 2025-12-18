"""
QUESTION:
Write a function named `reverse_sentence_words` that takes a sentence as input and returns the sentence with the order of characters in each word reversed, while maintaining the original position of each word within the sentence. The sentence can contain special characters and punctuation.
"""

def reverse_sentence_words(sentence):
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)