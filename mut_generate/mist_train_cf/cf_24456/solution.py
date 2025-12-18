"""
QUESTION:
Create a function named `substr` that takes a string as input and returns a list of all possible substrings of the given string. The function should include single characters as substrings and the empty string should be excluded from the output.
"""

def substr(s):
    """
    Returns a list of all possible substrings of the given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    list: A list of all possible substrings of the input string.
    """
    length = len(s)
    list_substr = []

    for w_index in range(length):
        for s_index in range(w_index + 1, length + 1):
            list_substr.append(s[w_index:s_index])

    return list_substr