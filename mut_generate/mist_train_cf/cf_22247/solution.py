"""
QUESTION:
Write a function `count_words` that takes a string as input and returns the number of words excluding "test" and its variations ("testing", "tested", etc.). The function should have a time complexity of O(n), where n is the length of the string.
"""

def count_words(input_string):
    """
    This function counts the number of words excluding "test" and its variations in a given string.
    
    Parameters:
    input_string (str): The input string to be processed.
    
    Returns:
    int: The number of words excluding "test" and its variations.
    """
    # Split the string into words
    words = input_string.split()
    
    # Initialize a count variable
    count = 0
    
    # Iterate over each word in the words list
    for word in words:
        # Check if the word is "test" or its variations
        if word.lower() not in ["test", "testing", "tested"]:
            # Increment the count variable
            count += 1
            
    # Return the count of words
    return count