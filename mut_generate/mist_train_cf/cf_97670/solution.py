"""
QUESTION:
Write a function `rearrange_sentence` that takes a list of words as input, where each word's first letter is capitalized, and returns a string representing a valid sentence. The function should properly handle spacing and punctuation. The input list contains words in random order, but the output sentence should be grammatically correct with a period at the end.
"""

def rearrange_sentence(words):
    # Join the words in the list to form a sentence
    sentence = ' '.join(words)
    
    # Add a period at the end of the sentence
    sentence += '.'
    
    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()
    
    return sentence