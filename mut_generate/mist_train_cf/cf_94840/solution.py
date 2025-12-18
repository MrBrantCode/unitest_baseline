"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a string `sentence` as input, reverses the order of the words, and keeps the order of characters within each word intact. The function should handle punctuation marks and multiple whitespaces between words. Implement the function with a time complexity of O(n), where n is the length of the input sentence, and without using any built-in string manipulation functions or methods (e.g. reverse, split, join).
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