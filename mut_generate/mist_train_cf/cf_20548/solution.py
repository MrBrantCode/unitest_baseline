"""
QUESTION:
Write a function named `sort_words` that takes a string as input, splits it into words, removes empty strings, removes leading/trailing whitespace from each word, and returns the words in descending order based on their length. Each word should contain at least two characters.
"""

def sort_words(string):
    """
    This function takes a string, splits it into words, removes empty strings, 
    removes leading/trailing whitespace from each word, and returns the words 
    in descending order based on their length. Each word should contain at least 
    two characters.
    
    Args:
        string (str): The input string.
    
    Returns:
        list: A list of words in descending order of their lengths.
    """
    # Split the string into a list of words and remove leading/trailing whitespace
    word_list = [word.strip() for word in string.split()]
    
    # Filter out the empty strings and words with less than 2 characters
    word_list = [word for word in word_list if len(word) >= 2]
    
    # Sort the words in descending order based on their length
    sorted_words = sorted(word_list, key=len, reverse=True)
    
    return sorted_words