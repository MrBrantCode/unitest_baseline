"""
QUESTION:
Write a function named `categorize_names` that groups a list of names into categories based on the length of the names and returns a dictionary with the categorized and sorted names. The dictionary should have keys from 1 to 5, representing the length of the names, and the corresponding values should be lists of names in reverse alphabetical order. If a category does not have any names, the key should still be present in the dictionary with an empty list as its value.
"""

def categorize_names(names):
    """
    This function groups a list of names into categories based on the length of the names.
    
    Args:
    names (list): A list of names
    
    Returns:
    dict: A dictionary with the categorized and sorted names
    """
    categories = {i: [] for i in range(1, 6)}
    
    for name in names:
        length = len(name)
        if 1 <= length <= 5:
            categories[length].append(name)
    
    for key in categories:
        categories[key].sort(reverse=True)
    
    return categories