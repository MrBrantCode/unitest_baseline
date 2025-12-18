"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of dictionaries and a key as input. The function should sort the list of dictionaries in ascending order based on the provided key, then remove any duplicates based on the same key. The function should return the sorted list of dictionaries without duplicates.
"""

def remove_duplicates(original_list, key):
    """
    Removes duplicates from a list of dictionaries based on a provided key.
    
    Args:
    original_list (list): A list of dictionaries.
    key (str): The key to remove duplicates based on.
    
    Returns:
    list: The sorted list of dictionaries without duplicates.
    """
    
    # Sort the list of dictionaries in ascending order based on the provided key
    sorted_list = sorted(original_list, key=lambda x: x[key])
    
    # Initialize an empty list to store the unique dictionaries
    result = []
    
    # Initialize an empty set to keep track of the values that have already been encountered
    seen = set()
    
    # Iterate over the sorted list of dictionaries
    for item in sorted_list:
        # Check if the value of the current dictionary based on the provided key has not been encountered before
        if item[key] not in seen:
            # Add the value to the set
            seen.add(item[key])
            # Append the current dictionary to the result list
            result.append(item)
    
    # Return the sorted list of dictionaries without duplicates
    return result