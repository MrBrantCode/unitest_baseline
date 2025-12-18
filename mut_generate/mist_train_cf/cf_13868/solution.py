"""
QUESTION:
Write a function called `longest_palindrome` that takes a string as input and returns the longest palindrome found in the string along with its length. The input string may contain punctuation, spaces, and uppercase letters. The function should ignore case and non-alphanumeric characters when searching for palindromes.
"""

def longest_palindrome(s):
    """
    This function finds the longest palindrome in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    tuple: A tuple containing the longest palindrome and its length.
    """
    
    # Remove non-alphanumeric characters and convert to lower case
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize variables to store the longest palindrome and its length
    longest_palindrome = ""
    max_length = 0
    
    # Iterate over the string
    for i in range(len(s)):
        # Check for odd length palindromes
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > max_length:
                longest_palindrome = substr
                max_length = len(substr)
                
    return longest_palindrome, max_length