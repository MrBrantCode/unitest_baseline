"""
QUESTION:
Write a Python function named `reverse_sentence` that takes a string sentence as input and returns a new sentence where each word is reversed while maintaining the original word order.
"""

def reverse_sentence(sentence):
    words = sentence.split(" ") 
    reversed_words = [word[::-1] for word in words] 
    reversed_sentence = ' '.join(reversed_words) 
    return reversed_sentence