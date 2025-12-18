"""
QUESTION:
Create a function called `isPalindrome` that takes a string as input and returns a boolean value. Implement the function using a recursive approach. The function should determine if the input string is a palindrome, considering only the characters and ignoring any case sensitivity, spaces, or punctuation.
"""

def isPalindrome(s: str) -> bool:
    """
    This function determines if the input string is a palindrome, 
    considering only the characters and ignoring any case sensitivity, 
    spaces, or punctuation.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """

    # Remove spaces and punctuation, and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Base case: Check if the length of the input string is 0 or 1
    if len(s) <= 1:
        return True
    
    # Recursive case: Compare the first and last characters of the string
    if s[0] != s[-1]:
        return False
    
    # If the first and last characters are equal, remove these characters 
    # from the string and call the isPalindrome function recursively 
    # with the updated string
    return isPalindrome(s[1:-1])