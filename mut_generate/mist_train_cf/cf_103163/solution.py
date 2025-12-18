"""
QUESTION:
Create a function called `categorize_names` that groups a list of names into 4 categories ('A', 'B', 'C', 'D') based on the first letter of each name. The function should sort the names in each category in alphabetical order and return the resulting dictionary. The function should be able to handle cases where the first letter of a name is not 'A', 'B', 'C', or 'D', in which case the name should not be included in the dictionary. The input list of names should be a list of strings, and the output should be a dictionary with string keys and list values.
"""

def categorize_names(names):
    """
    Groups a list of names into 4 categories ('A', 'B', 'C', 'D') based on the first letter of each name.
    
    Args:
        names (list): A list of strings representing names.
    
    Returns:
        dict: A dictionary with string keys ('A', 'B', 'C', 'D') and list values, where each list contains names in alphabetical order.
    """
    categories = {'A': [], 'B': [], 'C': [], 'D': []}
    
    for name in names:
        first_letter = name[0].upper()
        if first_letter in categories:
            categories[first_letter].append(name)
    
    for key in categories:
        categories[key].sort()
    
    return {key: value for key, value in categories.items() if value}