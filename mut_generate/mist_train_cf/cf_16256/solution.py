"""
QUESTION:
Write a function named `sum_unique_elements` that takes a list of integers `arr` as input. The function should return the sum of all unique elements in the list. The length of the input list is between 1 and 10^6, and each element is an integer between -10^9 and 10^9.
"""

def sum_unique_elements(arr):
    """
    This function calculates the sum of all unique elements in a given list of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of all unique elements in the list.
    """
    unique_elements = set()  # Create an empty hash set.
    total_sum = 0  # Initialize a variable to store the sum.
    
    # Iterate through each element in the input list.
    for num in arr:
        # If the element is not in the hash set, add it to the hash set and add it to the sum.
        if num not in unique_elements:
            unique_elements.add(num)
            total_sum += num
            
    return total_sum