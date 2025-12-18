"""
QUESTION:
Create a dictionary of 15 key-value pairs with fruit names as keys and their corresponding colors as values. Exactly three fruit names should be intentionally misspelled in the dictionary. Then, correct the misspelled names and sort the dictionary in reverse alphabetical order based on the corrected fruit names.
"""

def correct_and_sort_fruit_dict(fruit_dict):
    """
    Correct misspelled fruit names and sort the dictionary in reverse alphabetical order.
    
    Args:
        fruit_dict (dict): Dictionary with fruit names as keys and colors as values.
        
    Returns:
        dict: Dictionary with corrected fruit names and sorted in reverse alphabetical order.
    """
    
    # Define the correct spellings for misspelled fruit names
    corrections = {"appple": "apple", "orrange": "orange", "bluberry": "blueberry"}
    
    # Correct misspelled fruit names
    fruit_dict = {corrections.get(fruit, fruit): color for fruit, color in fruit_dict.items()}
    
    # Sort the dictionary in reverse alphabetical order
    fruit_dict = dict(sorted(fruit_dict.items(), key=lambda x: x[0], reverse=True))
    
    return fruit_dict