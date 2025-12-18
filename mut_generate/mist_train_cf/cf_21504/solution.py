"""
QUESTION:
Implement a function `reverse_string(s)` that reverses the input string `s` without using any built-in string reversal functions or methods. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The function should not use any additional data structures or arrays, and should be able to handle string inputs containing special characters, whitespace, and Unicode characters.
"""

def reverse_string(s):
    """
    Reverses the input string s without using any built-in string reversal functions or methods.
    
    Time complexity: O(n), where n is the length of the string
    Space complexity: O(n), as a list of characters is used for swapping
    
    Parameters:
    s (str): The input string to be reversed
    
    Returns:
    str: The reversed string
    """
    start = 0
    end = len(s) - 1
    
    # Convert the string to a list of characters for swapping
    s = list(s)
    
    # Swap characters until start is no longer less than end
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    # Convert the list of characters back to a string
    s = ''.join(s)
    
    return s