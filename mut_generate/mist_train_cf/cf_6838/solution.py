"""
QUESTION:
Write a function named find_max_value that takes a list of elements as input and returns the maximum value from the list. The function should handle lists containing integers, floats, and strings representing numbers. The function should consider strings as valid numbers if they represent a number when converted to float.
"""

def find_max_value(lst):
    """
    This function finds the maximum value from a list containing integers, floats, and strings representing numbers.
    
    Parameters:
    lst (list): A list of elements containing integers, floats, and strings representing numbers.
    
    Returns:
    max_value: The maximum value from the list.
    """
    
    # Initialize max_value as negative infinity to ensure any number in the list is larger
    max_value = float('-inf')
    
    # Iterate over each element in the list
    for element in lst:
        # Try to convert the element to float
        try:
            # If successful, update max_value if the element is larger
            max_value = max(max_value, float(element))
        # If not successful, skip this element
        except ValueError:
            continue
    
    # Return the maximum value
    return max_value