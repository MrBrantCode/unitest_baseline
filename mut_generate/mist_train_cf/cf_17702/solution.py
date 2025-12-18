"""
QUESTION:
Write a Python function called `reverse_sentence` that takes a sentence as input and returns the sentence with the order of the words reversed, while keeping the order of the characters within each word intact. The function should handle punctuation marks and multiple whitespaces between words. It must have a time complexity of O(n), where n is the length of the input sentence, and should not use any built-in string manipulation functions or methods (e.g. `reverse`, `split`, `join`).
"""

def reverse_sentence(sentence):
    reversed_sentence = ''
    word = ''
    for char in sentence:
        if char == ' ':
            reversed_sentence = word + char + reversed_sentence
            word = ''
        else:
            word += char
    reversed_sentence = word + ' ' + reversed_sentence
    return reversed_sentence.strip()