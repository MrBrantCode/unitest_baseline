"""
QUESTION:
Create a function called `invert_phrase` that takes a phrase as input and returns a string where each word in the phrase is reversed, while preserving the original word order. The phrase is a string of words separated by spaces, and the output should also be a string of words separated by spaces.
"""

def invert_phrase(phrase):
    # Split the phrase into individual words.
    words = phrase.split(" ")
    
    # Reverse each word and form a new list
    inverted_words = [word[::-1] for word in words]
    
    # Join the inverted words back into a sentence
    inverted_phrase = " ".join(inverted_words)
    
    return inverted_phrase