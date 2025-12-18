"""
QUESTION:
Create a function named `word_frequency` that takes a string `text` as input and returns the frequency of each word in the text. A word is defined as a sequence of characters separated by spaces, punctuation marks should be ignored, and the comparison of words should be case-insensitive. The output should be a list of words along with their frequencies, sorted in descending order based on frequency.
"""

def word_frequency(text):
    """
    Calculate the frequency of each word in the given text.

    Args:
    text (str): The input text.

    Returns:
    list: A list of tuples containing words and their frequencies, sorted in descending order by frequency.
    """
    
    # Remove punctuation and convert text to lowercase
    text = text.lower().replace('.', '').replace(',', '')
    words = text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the word_count dictionary by value in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_count