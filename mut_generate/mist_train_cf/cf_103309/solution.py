"""
QUESTION:
Create a function called `search_strings` that takes in an array of strings and a search term. The function should return an array of indices of strings that contain the exact word matching the search term, considering a case-sensitive search. The search should look for whole words, not substrings.
"""

def search_strings(array, search_term):
    """
    This function takes in an array of strings and a search term, 
    and returns an array of indices of strings that contain the exact word matching the search term.

    Args:
        array (list): A list of strings.
        search_term (str): The term to be searched.

    Returns:
        list: A list of indices of strings containing the search term.
    """
    indices = []
    for i in range(len(array)):
        words = array[i].split()
        if search_term in words:
            indices.append(i)
    return indices