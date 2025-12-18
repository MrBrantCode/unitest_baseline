"""
QUESTION:
Create a function named `create_sorted_dict` that generates a dictionary with unique alphanumeric keys and string values of minimum length 5. The dictionary must be sorted in ascending order based on the keys. The function should return the sorted dictionary.
"""

def create_sorted_dict(input_dict):
    """
    This function generates a dictionary with unique alphanumeric keys and string values of minimum length 5.
    The dictionary is sorted in ascending order based on the keys.

    Args:
        input_dict (dict): A dictionary with alphanumeric keys and string values.

    Returns:
        dict: A sorted dictionary based on the keys in ascending order.
    """
    # Sorting the dictionary based on keys in ascending order
    return {k: input_dict[k] for k in sorted(input_dict)}