"""
QUESTION:
Write a function named `search_keyword` that takes a dictionary and a keyword as input. The function should return a new dictionary containing the key-value pairs from the input dictionary where the keyword appears at the beginning of a word within the value. The function should not consider partial matches, i.e., the keyword must be at the start of a whole word in the value.
"""

def search_keyword(dictionary, keyword):
    """
    This function searches for a keyword in the values of a dictionary.
    
    Args:
        dictionary (dict): The input dictionary to be searched.
        keyword (str): The keyword to be searched in the dictionary values.
    
    Returns:
        dict: A new dictionary containing the key-value pairs from the input dictionary 
              where the keyword appears at the beginning of a word within the value.
    """
    
    matches = {}
    
    for key, value in dictionary.items():
        words = value.split()
        for word in words:
            if word.startswith(keyword):
                matches[key] = value
                break
    
    return matches