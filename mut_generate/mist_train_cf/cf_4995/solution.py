"""
QUESTION:
Implement a function named `reverse_string_recursive` that takes an input string `string` and reverses it recursively, maintaining the case of the original string. The function should not use any built-in string reversal functions or libraries. The time complexity should be O(n) and the space complexity should be O(1), where n is the length of the input string. The input string will only consist of uppercase and lowercase letters, and may contain leading or trailing spaces. The function should return the reversed string.
"""

def reverse_string_recursive(string):
    """
    Reverses a string recursively, maintaining the case of the original string.
    
    Args:
        string (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    def reverse(s, start, end):
        if start >= end:
            return s
        
        s = s[:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]
        
        return reverse(s, start+1, end-1)
    
    return reverse(string, 0, len(string)-1)