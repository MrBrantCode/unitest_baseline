"""
QUESTION:
Write a function `searchString` that takes two parameters, `text` and `pattern`, and returns the index position of the first occurrence of `pattern` in `text`. The function should be case-sensitive and return -1 if `pattern` is not found in `text`. The function should not use any built-in search functions or libraries and should have a time complexity of O(n), where n is the length of `text`.
"""

def searchString(text, pattern):
    """
    Searches for the first occurrence of a pattern in a given text.
    
    Args:
    text (str): The text to search in.
    pattern (str): The pattern to search for.
    
    Returns:
    int: The index position of the first occurrence of the pattern in the text. 
         Returns -1 if the pattern is not found.
    """
    
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        
        while j < m and text[i + j] == pattern[j]:
            j = j + 1
        
        if j == m:
            return i
    
    return -1