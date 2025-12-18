"""
QUESTION:
Create a function named longest_word_excluding_e that takes a string of words as input. The function should return the longest word that does not contain the letter "e". If multiple words have the same maximum length, return the first occurrence.
"""

def longest_word_excluding_e(s):
    """
    This function takes a string of words as input and returns the longest word 
    that does not contain the letter "e". If multiple words have the same maximum 
    length, it returns the first occurrence.

    Parameters:
    s (str): A string of words.

    Returns:
    str: The longest word excluding "e".
    """
    
    # Split the string into words
    words = s.split()
    
    # Initialize an empty string to store the longest word excluding "e"
    longest_word = ""
    
    # Iterate over each word in the list of words
    for word in words:
        # Check if the word does not contain the letter "e"
        if "e" not in word.lower():
            # Check if the length of the current word is greater than the length of the longest word found so far
            if len(word) > len(longest_word):
                # Update the longest word
                longest_word = word
                
    # Return the longest word excluding "e"
    return longest_word