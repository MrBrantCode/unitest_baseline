"""
QUESTION:
Create a function named `search_for_nn` and `search_for_vbp` that takes a tuple containing a word and its part of speech tag as input, where the word is a noun (NN) or verb in the present tense, not third person singular (VBP), respectively. The function should return a string representing the result of the search for the given word.
"""

def search_for_nn(word_tuple):
    # Process the query and search for nouns (NN)
    # Return the result as a string
    return f"Found noun: {word_tuple[0]}"

def search_for_vbp(word_tuple):
    # Process the query and search for verbs in the present tense, not third person singular (VBP)
    # Return the result as a string
    return f"Found verb: {word_tuple[0]}"