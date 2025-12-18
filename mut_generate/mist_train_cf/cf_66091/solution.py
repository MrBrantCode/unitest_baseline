"""
QUESTION:
Create a function named `reverse_sequence` that takes three strings of numeric characters as input and returns a single string formed by reversing the combined sequence of the input strings.
"""

def reverse_sequence(numString1, numString2, numString3):
    """
    This function takes three strings of numeric characters, combines them into a single string, 
    and returns the reversed sequence of the combined string.
    
    Parameters:
    numString1 (str): The first string of numeric characters.
    numString2 (str): The second string of numeric characters.
    numString3 (str): The third string of numeric characters.
    
    Returns:
    str: A single string formed by reversing the combined sequence of the input strings.
    """
    # Combine all the strings
    combinedString = numString1 + numString2 + numString3
    
    # Reverse the combined string
    reversedString = combinedString[::-1]
    
    return reversedString