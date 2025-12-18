"""
QUESTION:
Write a function `count_occurrences` that takes a number and a nested list as input and returns the number of occurrences of the number in the list, ignoring any occurrences within sublists. The function should handle cases where the number is a float, return an error message if the number is not a valid float, and consider negative floats as valid.
"""

def count_occurrences(number, nested_list):
    """
    Counts the number of occurrences of a number in a nested list, ignoring occurrences within sublists.
    
    Args:
        number (float): The number to count occurrences of.
        nested_list (list): The nested list to search in.
    
    Returns:
        int: The number of occurrences of the number in the list, or an error message if the number is not a valid float.
    """
    count = 0

    # Check if the number is a valid float
    try:
        float(number)
    except ValueError:
        return "Error: Invalid float number"

    # Helper function to recursively count occurrences
    def count_recursive(lst):
        nonlocal count
        for item in lst:
            if isinstance(item, list):
                count_recursive(item)
            elif item == number:
                count += 1

    # Call the helper function to count occurrences
    count_recursive(nested_list)

    return count