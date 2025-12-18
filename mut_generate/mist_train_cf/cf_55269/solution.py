"""
QUESTION:
Create two functions, `count_elements` and `sum_elements`, that operate on a potentially nested dictionary structure. 

`count_elements` should recursively calculate and return the total quantity of elements in the dictionary structure. 

`sum_elements` should recursively sum all the integer values present in the dictionary structure, ignoring non-integer values. 

The functions should handle unexpected inputs and edge cases efficiently, including non-integer values within nested dictionaries and larger, more complex dictionary structures.
"""

def count_elements(some_dict):
    """
    Recursively calculate and return the total quantity of elements in a dictionary structure.
    
    Args:
        some_dict (dict): The dictionary structure to count elements in.
    
    Returns:
        int: The total quantity of elements in the dictionary structure.
    """
    count = 0
    for key, value in some_dict.items():
        if isinstance(value, dict): 
            count += count_elements(value)
        else:
            count += 1 
    return count


def sum_elements(some_dict):
    """
    Recursively sum all the integer values present in a dictionary structure, ignoring non-integer values.
    
    Args:
        some_dict (dict): The dictionary structure to sum integer values in.
    
    Returns:
        int: The sum of all integer values in the dictionary structure.
    """
    total_sum = 0
    for key, value in some_dict.items():
        if isinstance(value, dict): 
            total_sum += sum_elements(value)
        elif isinstance(value, int): 
            total_sum += value
    return total_sum