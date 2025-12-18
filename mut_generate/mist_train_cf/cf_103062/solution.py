"""
QUESTION:
Write a function `find_longest_word` that takes an array of strings as input and returns the word with the maximum length. Also, calculate the total length of all words in the array. The function should be able to handle any number of strings in the input array.
"""

def find_longest_word(arr):
    """
    This function finds the longest word in an array of strings and calculates the total length of all words.
    
    Parameters:
    arr (list): A list of strings.
    
    Returns:
    tuple: A tuple containing the longest word and the total length of all words.
    """
    max_length = 0
    longest_word = ""
    total_length = 0
    
    for word in arr:
        total_length += len(word)
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
            
    return longest_word, total_length