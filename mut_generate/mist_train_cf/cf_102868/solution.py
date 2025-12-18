"""
QUESTION:
Write a function named `find_min_element_frequency` that takes an array of integers as input and returns the minimum element and its frequency. The array is guaranteed to have at least one duplicate element.
"""

def find_min_element_frequency(arr):
    """
    This function takes an array of integers as input, and returns the minimum element and its frequency.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the minimum element and its frequency.
    """
    min_element = float('inf')
    element_frequency = {}
    
    # Iterate through each element in the array to find the minimum element and update its frequency
    for num in arr:
        if num < min_element:
            min_element = num
        element_frequency[num] = element_frequency.get(num, 0) + 1
    
    # Find the maximum frequency
    frequency = max(element_frequency.values())
    
    return min_element, frequency