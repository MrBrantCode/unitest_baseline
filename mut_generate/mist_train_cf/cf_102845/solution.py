"""
QUESTION:
Create a function `create_array` that constructs an array of N elements from a given string, where N is the length of the string. The function should have a time complexity of O(N) and a space complexity of O(N).
"""

def create_array(string):
    """
    Construct an array of N elements from a given string, where N is the length of the string.
    
    Time complexity: O(N), where N is the length of the string.
    Space complexity: O(N), where N is the length of the string.
    
    Args:
        string (str): The input string.
    
    Returns:
        list: A list of characters in the input string.
    """
    return [char for char in string]