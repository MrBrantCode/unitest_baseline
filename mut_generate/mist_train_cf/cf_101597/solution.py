"""
QUESTION:
Write a function named `reverse_sentence` that takes a sentence as input and returns the sentence with its words in reverse order. The function should handle sentences with multiple words and return a properly formatted sentence with the first letter capitalized and a period at the end.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words).capitalize() + '.'