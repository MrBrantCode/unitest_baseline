"""
QUESTION:
Implement a function named `resize_dict` that efficiently resizes a dictionary in Python by handling hash collisions and maintaining memory allocation efficiency. The function should take in the dictionary and its current size as input and return the resized dictionary and its new size. The function should use a load factor of 0.66 to determine when the dictionary needs to be resized.
"""

def resize_dict(dictionary, current_size):
    """
    Resizes a dictionary by handling hash collisions and maintaining memory allocation efficiency.
    
    Args:
    dictionary (dict): The dictionary to be resized.
    current_size (int): The current size of the dictionary.
    
    Returns:
    dict, int: A tuple containing the resized dictionary and its new size.
    """
    
    # Calculate the load factor (number of keys / current size)
    load_factor = len(dictionary) / current_size
    
    # Check if the load factor exceeds 0.66
    if load_factor > 0.66:
        # Calculate the new size as the next power of 2
        new_size = 2 ** (current_size.bit_length() + 1)
        
        # Create a new dictionary with the new size
        new_dict = dict()
        
        # Iterate over the key-value pairs in the old dictionary
        for key, value in dictionary.items():
            # Compute the new index using the new size
            new_index = hash(key) % new_size
            
            # Handle collisions using linear probing
            while new_index in new_dict:
                new_index = (new_index + 1) % new_size
            
            # Insert the key-value pair into the new dictionary
            new_dict[new_index] = value
        
        # Return the resized dictionary and its new size
        return new_dict, new_size
    
    # If the load factor does not exceed 0.66, return the original dictionary and its size
    return dictionary, current_size