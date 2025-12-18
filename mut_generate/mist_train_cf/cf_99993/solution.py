"""
QUESTION:
Write a function named `rearrange_sentence` that takes a list of words as input, where the first letter of each word is always capitalized. The function should return a string sentence with proper punctuation (a period at the end) and spacing (a space between each word).
"""

def rearrange_sentence(words):
    # Join the words in the list to form a sentence
    sentence = ' '.join(words)
 
    # Add a period at the end of the sentence
    sentence += '.'
 
    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()
 
    return sentence