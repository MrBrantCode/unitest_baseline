"""
QUESTION:
Create a function `count_substrings` that takes a text string as input and returns a dictionary with unique sub-strings of length 3 as keys and their corresponding frequencies as values. The function should ignore spaces and punctuation, and be case-insensitive. If no such sub-strings of length 3 exist, return a message indicating this.
"""

import re
from collections import Counter

def count_substrings(text):
    """
    This function takes a text string as input and returns a dictionary with unique sub-strings of length 3 as keys and their corresponding frequencies as values.
    
    Parameters:
    text (str): The input text string
    
    Returns:
    dict: A dictionary with unique sub-strings of length 3 as keys and their corresponding frequencies as values.
    """
    
    # Convert the text to lower case and remove non-alphanumeric characters
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', text).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Iterate over each word in the text
    for word in words:
        # Iterate over the characters in the word
        for i in range(len(word) - 2):
            # Extract the substring of length 3 and add it to the list
            substrings.append(word[i:i+3])
    
    # Use the Counter class to count the frequency of each substring
    frequency = Counter(substrings)
    
    # If no substrings of length 3 exist, return a message indicating this
    if len(frequency) == 0:
        return "No substrings of length 3 found in the text."
    else:
        # Return the dictionary with the frequency of each substring
        return dict(frequency)