"""
QUESTION:
Write a function named `duplicate_words` that takes a string `sentence` and an integer `num` as input. The function should return a new string where each word in the original sentence is duplicated `num` times consecutively, while maintaining the original word order.
"""

def duplicate_words(sentence, num):
    words = sentence.split(' ')
    duplicated_words = ' '.join([' '.join([word]*num) if word != '' else '' for word in words])
    return duplicated_words