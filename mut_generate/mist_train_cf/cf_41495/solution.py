"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input and returns a dictionary containing the frequency of each word in the text. A word is defined as a sequence of characters separated by spaces, and all words should be treated as case-insensitive. The function should ignore any punctuation marks and consider words with different capitalization as the same word. The output dictionary should be sorted in alphabetical order based on the words.
"""

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    frequency_dict = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    # Sort the dictionary by keys
    sorted_frequency_dict = dict(sorted(frequency_dict.items()))
    
    return sorted_frequency_dict