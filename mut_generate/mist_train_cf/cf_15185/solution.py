"""
QUESTION:
Write a function `is_anagram` that checks whether two input strings are anagrams or not, considering all characters (including upper and lower case alphabets, numbers, and special characters), ignoring case sensitivity, and handling leading and trailing whitespace characters. The function should have a time complexity of O(n), where n is the length of the longest string, and return True if the strings are anagrams and False otherwise.
"""

def is_anagram(first, second):
    """
    Checks whether two input strings are anagrams or not, considering all characters 
    (including upper and lower case alphabets, numbers, and special characters), 
    ignoring case sensitivity, and handling leading and trailing whitespace characters.

    Args:
    first (str): The first input string.
    second (str): The second input string.

    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """

    # Remove leading and trailing whitespace characters
    first = first.strip()
    second = second.strip()
    
    # Convert both strings to lowercase
    first = first.lower()
    second = second.lower()
    
    # Remove all non-alphanumeric characters
    first = ''.join(e for e in first if e.isalnum())
    second = ''.join(e for e in second if e.isalnum())
    
    # Check if the lengths of the strings are equal
    if len(first) != len(second):
        return False
    
    # Create dictionaries to count the frequency of each character
    first_dict = {}
    second_dict = {}
    
    # Count the frequency of each character in the first string
    for char in first:
        if char in first_dict:
            first_dict[char] += 1
        else:
            first_dict[char] = 1
    
    # Count the frequency of each character in the second string
    for char in second:
        if char in second_dict:
            second_dict[char] += 1
        else:
            second_dict[char] = 1
    
    # Check if the dictionaries are equal
    return first_dict == second_dict