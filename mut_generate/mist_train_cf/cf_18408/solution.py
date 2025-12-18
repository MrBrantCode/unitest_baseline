"""
QUESTION:
Create a function `are_anagrams(string1, string2)` that determines if two input strings are anagrams of each other. The function should be case-insensitive, handle special characters and spaces, and have a time complexity of O(n) where n is the length of the strings. The function should not use any built-in sorting functions or libraries. The function should be able to handle strings of length up to 10^6.
"""

def are_anagrams(string1, string2):
    """
    Determines if two input strings are anagrams of each other.
    
    The function is case-insensitive, handles special characters and spaces, 
    and has a time complexity of O(n) where n is the length of the strings.
    
    Parameters:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Remove spaces and special characters from both strings
    string1 = ''.join(e for e in string1 if e.isalnum())
    string2 = ''.join(e for e in string2 if e.isalnum())

    # Check if the lengths of the two strings are equal
    if len(string1) != len(string2):
        return False

    # Create a dictionary to store the frequency of each character in string1
    char_frequency = {}

    # Count the frequency of each character in string1
    for char in string1:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Check if the frequency of characters in string2 matches the frequency in string1
    for char in string2:
        if char in char_frequency:
            char_frequency[char] -= 1
            if char_frequency[char] == 0:
                del char_frequency[char]
        else:
            return False

    # If all characters in string2 have been matched and removed from char_frequency, they are anagrams
    return not char_frequency