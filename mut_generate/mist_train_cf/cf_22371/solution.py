"""
QUESTION:
Write a function named `reverse_string` that takes two parameters: a string and its length. The function should print the string in reverse order with no duplicate characters and return the count of unique characters in the reversed string.
"""

def reverse_string(s, length):
    """
    This function takes a string and its length as parameters, 
    prints the string in reverse order with no duplicate characters, 
    and returns the count of unique characters in the reversed string.
    
    Parameters:
    s (str): The input string
    length (int): The length of the input string
    
    Returns:
    int: The count of unique characters in the reversed string
    """
    reversed_string = s[::-1]
    unique_chars = set(reversed_string)
    print("Reversed string:", "".join(unique_chars))
    return len(unique_chars)