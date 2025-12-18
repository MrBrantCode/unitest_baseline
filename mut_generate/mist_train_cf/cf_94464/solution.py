"""
QUESTION:
Create a function `sentence_reverse(sentence)` that takes a string as input, removes leading and trailing whitespaces, and returns the input string with the order of its words reversed. The input string may contain special characters, punctuation, and multiple whitespaces.
"""

def sentence_reverse(sentence):
    # Remove leading and trailing whitespaces
    sentence = sentence.strip()
    
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Reverse the order of the words in the list
    words = words[::-1]
    
    # Join the words in the reversed order with spaces between them
    reversed_sentence = ' '.join(words)
    
    return reversed_sentence