"""
QUESTION:
Create a function `word_frequency` that takes a string `text` as input and returns a dictionary with the frequency of each word in the text. The function should also identify and return the top 3 most frequently occurring words. Note that the function should consider words as case-sensitive and should not ignore any words.
"""

def word_frequency(text):
    """
    This function calculates the frequency of each word in the given text and returns the top 3 most frequently occurring words.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    dict: A dictionary containing the frequency of each word.
    """
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store the frequency of each word
    frequency = {}
    
    # Iterate over each word in the text
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            frequency[word] = 1
    
    # Sort the dictionary by values in descending order and get the top 3 most frequently occurring words
    top_3_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Return the frequency dictionary and the top 3 most frequently occurring words
    return frequency, top_3_words