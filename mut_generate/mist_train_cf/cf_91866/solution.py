"""
QUESTION:
Write a function named `count_unique_words` that takes a string `sentence` as input and returns the total number of unique words in the sentence, excluding any repeated words. The function should consider two words as the same if they are identical, regardless of case, but it is not explicitly stated in the problem, so it should be case-sensitive.
"""

def count_unique_words(sentence):
    """
    Returns the total number of unique words in the given sentence.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    int: The total number of unique words in the sentence.
    """
    # Split the sentence into individual words
    words = sentence.split()
    
    # Create a set to store unique words
    unique_words = set(words)
    
    # Return the total number of unique words
    return len(unique_words)