"""
QUESTION:
Write a function `find_longest_substring` that finds the longest substring of a given string with a length of 2 or more characters without any repeating letters. The function should return the longest substring that meets this condition.
"""

def find_longest_substring(string):
    """
    Finds the longest substring of a given string with a length of 2 or more characters without any repeating letters.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The longest substring without repeating letters.
    """
    start_index = 0
    visited = set()
    length = 0
    result = ""
    
    for i in range(len(string)):
        if string[i] in visited:
            visited.remove(string[start_index])
            start_index += 1
            
        visited.add(string[i])
        
        if length < i - start_index + 1 and i - start_index + 1 >= 2:
            length = i - start_index + 1
            result = string[start_index:i+1]
        
    return result