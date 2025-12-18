"""
QUESTION:
Create a function called `rearrange_sentence` that takes a list of words as input where each word has its first letter capitalized. The function should return a string with the words rearranged into a grammatically correct sentence with proper punctuation and spacing.
"""

def rearrange_sentence(words):
    # Join the words in the list to form a sentence
    sentence = ' '.join(words)
    
    # Add a period at the end of the sentence
    sentence += '.'
    
    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()
    
    return sentence