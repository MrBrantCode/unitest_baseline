"""
QUESTION:
Write a function called `update_words` that takes an array of strings as input. The function should replace each word with more than 7 characters with its uppercase version and remove words with 7 or less characters that were converted to uppercase. Then, it should return the updated array sorted in ascending order by the length of the words.
"""

def update_words(words):
    """
    This function updates the input list of words by replacing each word with more than 7 characters 
    with its uppercase version and removing words with 7 or less characters that were converted to 
    uppercase. Then, it returns the updated list sorted in ascending order by the length of the words.

    Args:
        words (list): A list of strings

    Returns:
        list: The updated list of words
    """
    # Filter out words with length 7 or less and convert longer words to uppercase
    words = [word.upper() if len(word) > 7 else None for word in words if len(word) > 7 or word.islower()]
    
    # Remove None values
    words = [word for word in words if word is not None]
    
    # Sort the words based on their length
    words.sort(key=len)
    
    return words