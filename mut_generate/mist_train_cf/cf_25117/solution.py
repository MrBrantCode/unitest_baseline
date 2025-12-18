"""
QUESTION:
Write a function `count_substrings` that takes a string `sentence` as input and returns the number of substrings of length 3 present in the sentence. The input sentence is a sequence of words separated by spaces and the substrings can be any sequence of 3 characters.
"""

def count_substrings(sentence):
    """
    Returns the number of substrings of length 3 present in the sentence.
    
    Args:
        sentence (str): A sequence of words separated by spaces.
    
    Returns:
        int: The number of substrings of length 3.
    """
    # Remove spaces from the sentence to consider the entire sentence as a single sequence of characters
    sentence = sentence.replace(" ", "")
    
    # Initialize a counter for the number of substrings
    count = 0
    
    # Iterate over the characters in the sentence
    for i in range(len(sentence) - 2):
        # Increment the counter for each substring of length 3
        count += 1
    
    # Return the total count of substrings
    return count