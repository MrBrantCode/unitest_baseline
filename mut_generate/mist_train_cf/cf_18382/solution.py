"""
QUESTION:
Write a function named `reverse_sentence` that takes a string input and returns the reversed sentence without using any built-in string reverse functions or methods, additional data structures, or string manipulation methods. The function should reverse the order of words in the sentence.
"""

def reverse_sentence(sentence):
    reversed_sentence = ''
    word = ''
    for i in range(len(sentence)-1, -1, -1):
        if sentence[i] != ' ':
            word = sentence[i] + word
        else:
            reversed_sentence += word + ' '
            word = ''
    reversed_sentence += word
    return reversed_sentence