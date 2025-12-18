"""
QUESTION:
Write a function named `count_unique_words` that takes a string as input. The function should return the count of unique words in the string, excluding any words that contain the letter 'a' and have more than 5 characters. The unique words should be sorted in descending order of their length, and in case of a tie, sorted alphabetically.
"""

def count_unique_words(s):
    """
    This function takes a string as input, excludes any words that contain the letter 'a' and have more than 5 characters,
    and returns the count of unique words in descending order of their length, and in case of a tie, sorted alphabetically.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The count of unique words.
    """
    
    # Split the string into words and convert to lower case
    words = s.lower().split()
    
    # Filter out words that contain 'a' and have more than 5 characters
    filtered_words = [word for word in words if 'a' not in word or len(word) <= 5]
    
    # Use set to get unique words
    unique_words = set(filtered_words)
    
    # Sort the unique words in descending order of their length, and in case of a tie, sort alphabetically
    sorted_unique_words = sorted(unique_words, key=lambda x: (-len(x), x))
    
    # Return the count of unique words
    return len(sorted_unique_words)