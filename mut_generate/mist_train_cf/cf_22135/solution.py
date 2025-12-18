"""
QUESTION:
Write a function `char_frequency` that takes a string as input, calculates the frequency of each alphabetic character in the string (ignoring case sensitivity), and returns the frequencies sorted in descending order of the characters' ASCII values. The function should ignore non-alphabetic characters.
"""

def char_frequency(s):
    """
    Calculate the frequency of each alphabetic character in the string (ignoring case sensitivity) 
    and return the frequencies sorted in descending order of the characters' ASCII values.
    
    Parameters:
    s (str): Input string
    
    Returns:
    dict: A dictionary containing the frequency of each alphabetic character
    """
    
    # Convert the string to lowercase
    s = s.lower()
    
    # Create a dictionary to store the frequencies
    frequency = {}
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is an alphabet
        if char.isalpha():
            # Update the frequency dictionary
            frequency[char] = frequency.get(char, 0) + 1
    
    # Sort the characters by their ASCII values in descending order
    sorted_chars = sorted(frequency.keys(), key=lambda x: ord(x), reverse=True)
    
    # Create a dictionary to store the sorted frequencies
    sorted_frequency = {char: frequency[char] for char in sorted_chars}
    
    return sorted_frequency