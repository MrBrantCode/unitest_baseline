"""
QUESTION:
Create a function named `create_name_dict` that takes a list of names as input and returns a dictionary. The function should ignore names containing numbers or special characters, remove duplicates, and only consider names with a length of at least 3 characters. The dictionary should have the names as keys and their lengths as values, sorted in descending order of the lengths.
"""

def create_name_dict(names):
    # Remove duplicate names and names with special characters
    filtered_names = list(set([name for name in names if name.isalpha() and len(name) >= 3]))
    
    # Sort the names in descending order based on length
    filtered_names.sort(key=lambda x: len(x), reverse=True)
    
    # Create the dictionary with names as keys and lengths as values
    return {name: len(name) for name in filtered_names}