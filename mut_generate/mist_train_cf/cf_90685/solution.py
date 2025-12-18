"""
QUESTION:
Write a function `remove_duplicates_and_sort` that takes a string as input, removes all duplicate characters, and returns the remaining characters in a string sorted in ascending order based on their ASCII values. The function should ignore case sensitivity and consider spaces and special characters as valid characters. If there are no remaining characters after removing duplicates, the function should return an empty string.
"""

def remove_duplicates_and_sort(string):
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Remove duplicates using a set
    string = ''.join(set(string))
    
    # Sort the remaining characters in ascending order based on ASCII values
    sorted_string = ''.join(sorted(string))
    
    return sorted_string