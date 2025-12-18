"""
QUESTION:
Design a function `are_anagrams` that checks if two input strings are anagrams of each other. The function should be case-insensitive and consider special characters and numbers. It should return `True` if the strings are anagrams and `False` otherwise. The function should be able to handle large strings efficiently.
"""

def are_anagrams(string1, string2):
    """
    Checks if two input strings are anagrams of each other.
    
    This function is case-insensitive and considers special characters and numbers.
    It returns True if the strings are anagrams and False otherwise.
    
    Parameters:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    bool: Whether the two strings are anagrams.
    """
    
    # First, make all characters lower case and remove leading and trailing spaces
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # If lengths of both strings are not equal, they cannot be anagrams
    if len(string1) != len(string2):
        return False

    # Create a hash map (dictionary) to store count of characters
    count = {}

    # Iterate through each character in first string
    for char in string1:
        # If character is already in dictionary, increment count, else add to dictionary with count 1
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Now, iterate through each character in second string
    for char in string2:
        # If character is not in dictionary or count becomes 0, return False
        if char not in count or count[char] == 0:
            return False
        # Else decrement the count
        else:
            count[char] -= 1

    # If we reached here, strings are anagrams
    return True