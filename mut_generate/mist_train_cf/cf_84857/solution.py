"""
QUESTION:
Create a function named `word_frequency` that takes two parameters: a sentence and a word. The function should calculate the frequency of the given word in the sentence, considering a case-insensitive comparison. The sentence can contain multiple words separated by spaces, and the function should return the number of times the word appears in the sentence.
"""

def word_frequency(sentence, word):
    """
    Calculate the frequency of a word in a sentence.
    
    Parameters:
    sentence (str): The input sentence.
    word (str): The word to find the frequency of.
    
    Returns:
    int: The frequency of the word in the sentence.
    """
    # Change the sentence to lowercase to assure case insensitivity
    sentence = sentence.lower()
    word = word.lower()  # Also convert the word to lowercase for case-insensitive comparison
    
    # Convert the sentence into a list of words
    words = sentence.split()
    
    # Count the word frequency
    frequency = words.count(word)
    return frequency