"""
QUESTION:
Create a function called `rearrange_sentence` that takes a list of words as input, where each word's first letter is capitalized, and returns a valid sentence as a string. The words in the list are in random order, and the output sentence should have proper punctuation and spacing.
"""

def rearrange_sentence(words):
    # Join the words in the list to form a sentence
    sentence = ' '.join(words)
    
    # Add a period at the end of the sentence
    sentence += '.'
    
    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()
    
    return sentence