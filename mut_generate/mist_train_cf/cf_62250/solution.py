"""
QUESTION:
Remove extra spaces from a given string, ensuring a uniform single space between words.

Create a function named `eliminate_spaces` that takes a string as input and returns the modified string with no leading, trailing, or duplicate spaces, and exactly one space between each word.
"""

def eliminate_spaces(sentence):
    words = sentence.split()
    new_sentence = ' '.join(words)
    return new_sentence