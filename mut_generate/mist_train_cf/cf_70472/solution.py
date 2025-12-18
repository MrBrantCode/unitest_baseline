"""
QUESTION:
Write a function called `reverse_sentence` that takes a string input and returns a string with the order of the words reversed. For example, the input "Hello world this is Python" should result in "Python is this world Hello". The function should preserve the original orientation of individual characters within the words.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    words = words[::-1]
    return " ".join(words)