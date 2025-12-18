"""
QUESTION:
Create a function called `sentence_reverse` that takes a string sentence as input and returns the sentence in reverse order as a string. The function should handle sentences with leading or trailing whitespaces, special characters, punctuation, and multiple whitespaces, without using built-in string reversal functions or methods.
"""

def sentence_reverse(sentence):
    # Trim any leading or trailing whitespaces from the input sentence
    sentence = sentence.strip()
    
    # Initialize an empty list to store the characters of the sentence in reverse order
    reversed_sentence = []
    
    # Iterate over each character in the input sentence
    for char in sentence:
        # Insert each character at the beginning of the list
        reversed_sentence.insert(0, char)
    
    # Join the reversed characters back together into a single string
    reversed_sentence = ''.join(reversed_sentence)
    
    return reversed_sentence