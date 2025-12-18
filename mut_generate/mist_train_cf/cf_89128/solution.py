"""
QUESTION:
Write a function `update_words` that takes an array of strings as input, removes words with more than 7 characters and replaces them with their uppercase equivalent, and returns the updated array sorted in ascending order based on the length of the words. The input array contains only strings and the function should not take any additional parameters.
"""

def update_words(words):
    """
    This function takes an array of strings, removes words with more than 7 characters 
    and replaces them with their uppercase equivalent, and returns the updated array 
    sorted in ascending order based on the length of the words.
    
    Parameters:
    words (list): The input list of strings.
    
    Returns:
    list: The updated list of strings.
    """
    # Remove words with length greater than 7 and convert them to uppercase
    updated_words = [word.upper() if len(word) > 7 else word for word in words]
    
    # Sort the words based on their length
    updated_words.sort(key=len)
    
    return updated_words