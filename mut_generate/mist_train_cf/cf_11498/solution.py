"""
QUESTION:
Write a function named `count_unique_words` that takes a string `sentence` as input and returns the total number of unique words in the sentence, excluding any repeated words.
"""

def count_unique_words(sentence):
    """
    Returns the total number of unique words in a given sentence.

    Args:
    sentence (str): The input sentence.

    Returns:
    int: The total number of unique words in the sentence.
    """
    # Split the sentence into individual words
    words = sentence.split()

    # Create a set to store unique words
    unique_words = set()

    # Iterate through each word and add it to the set
    for word in words:
        unique_words.add(word)

    # Return the total number of unique words
    return len(unique_words)