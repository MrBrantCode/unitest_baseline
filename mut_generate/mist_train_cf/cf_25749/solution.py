"""
QUESTION:
Implement a function `word_frequency` that tracks the frequency of words in a given text. The function should accept a string of text as input and return a data structure where the keys are the unique words in the text and the values are their corresponding frequencies. The function should have a time complexity of O(1) for retrieving the frequency of a given word.
"""

def word_frequency(text):
    """
    Tracks the frequency of words in a given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        dict: A dictionary where the keys are the unique words in the text and the values are their corresponding frequencies.
    """
    # Split the text into words, ignoring case and non-alphanumeric characters
    words = ''.join(e for e in text if e.isalnum() or e.isspace()).lower().split()
    
    # Create a dictionary to store word frequencies
    frequency = {}
    
    # Iterate over each word in the text
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            frequency[word] = 1
    
    return frequency