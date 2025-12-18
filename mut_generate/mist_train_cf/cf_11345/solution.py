"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a string sentence as input and returns the reversed sentence. The function should not use any built-in string reverse functions or methods. It should reverse the order of the words in the sentence, with each word and space in its original form.
"""

def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    reversed_sentence = " ".join(reversed_words)  
    return reversed_sentence