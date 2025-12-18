"""
QUESTION:
Develop a function `generate_phrases` that takes a list of words as input and returns a list of all possible five-word phrases that can be formed by combining these words. The function should exclude phrases containing the word sequences "drip echo" or "echo drip" and return the remaining phrases in alphabetical order.

The input list of words is ["rain", "drip", "echo", "crackle", "splash"]. The function should be able to handle this list of words and return the corresponding phrases.
"""

import itertools

def generate_phrases(words):
    # Generate all possible combinations of five words
    combinations = itertools.combinations(words, 5)
    # Define a list to store the valid phrases
    phrases = []
    # Loop through each combination of words
    for combo in combinations:
        # Combine the words into a phrase
        phrase = " ".join(combo)
        # Check if the phrase makes sense
        if "drip echo" in phrase or "echo drip" in phrase:
            continue
        # Add the phrase to the list if it makes sense
        phrases.append(phrase)
    # Sort the list of phrases in alphabetical order
    phrases.sort()
    return phrases