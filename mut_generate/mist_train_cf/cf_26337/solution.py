"""
QUESTION:
Create a function called `reverse_words` that takes a string sentence as input. The function should reverse the order of characters in each word, but keep the words in their original order within the sentence. The input sentence can contain multiple words separated by spaces.
"""

def reverse_words(sentence):
    words = sentence.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)