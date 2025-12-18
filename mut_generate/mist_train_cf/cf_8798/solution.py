"""
QUESTION:
Write a function `calculate_sum` that takes a list of integers as input, calculates the sum of its unique elements, and returns the result. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(n), where n is the number of unique elements in the list. The input list may be empty, contain duplicates, and have both positive and negative integers. Do not use any built-in functions or libraries that directly calculate the sum of a list.
"""

def calculate_sum(my_list):
    """
    Calculate the sum of unique elements in a list.
    
    Args:
        my_list (list): A list of integers.
    
    Returns:
        int: The sum of unique elements in the list.
    """
    # Create a dictionary to store the unique elements as keys
    unique_elements = {}
    
    # Iterate through the list and add the elements to the dictionary
    for num in my_list:
        unique_elements[num] = num
    
    # Calculate the sum of the unique elements
    return sum(unique_elements.values())