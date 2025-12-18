"""
QUESTION:
Write a function named `reverse_sentence` that takes a string parameter `sentence` and returns the reversed sentence. The function should not use any built-in string reverse functions or methods, additional data structures (e.g., lists, dictionaries), or string manipulation methods (e.g., join(), split()).
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