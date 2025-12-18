"""
QUESTION:
Write a function `count_letters` that takes a string as input and returns a dictionary with the number of occurrences of each letter in the string, disregarding case sensitivity and excluding non-alphabetic characters.
"""

def count_letters(s):
    """
    This function takes a string as input and returns a dictionary with the number of occurrences of each letter in the string,
    disregarding case sensitivity and excluding non-alphabetic characters.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where the keys are the letters in the string and the values are their corresponding counts.
    """
    
    # Convert the string to lowercase to disregard case sensitivity
    s = s.lower()
    
    # Remove non-alphabetic characters
    s = ''.join(char for char in s if char.isalpha())
    
    # Initialize an empty dictionary to store the count of each letter
    letter_count = {}
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is already in the dictionary
        if char in letter_count:
            # Increment its count by 1
            letter_count[char] += 1
        else:
            # Add the character as a new key with a count of 1
            letter_count[char] = 1
            
    # Return the dictionary
    return letter_count