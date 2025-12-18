"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input and returns a list of unique words in the text along with their frequencies. The comparison of words should be case-insensitive and punctuation marks should be ignored. The output list should be sorted in descending order based on frequency.
"""

def word_frequency(text):
    """
    Returns a list of unique words in the text along with their frequencies.
    
    The comparison of words is case-insensitive and punctuation marks are ignored.
    The output list is sorted in descending order based on frequency.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    list: A list of tuples containing unique words and their frequencies.
    """
    # Remove punctuation and convert text to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_freq