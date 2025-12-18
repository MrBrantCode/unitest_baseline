"""
QUESTION:
Combine two lists into one sorted list without duplicates.

Write a function named `combine_lists` that takes two lists of integers as input and returns a single sorted list containing all unique elements from both lists. The function must implement its own sorting and duplicate removal logic without using built-in Python functions for sorting or removing duplicates.
"""

def combine_lists(list_one, list_two):
    """
    This function combines two lists into one sorted list without duplicates.
    
    Args:
        list_one (list): The first list of integers.
        list_two (list): The second list of integers.
    
    Returns:
        list: A single sorted list containing all unique elements from both lists.
    """
    
    # Combine the two lists into one
    combined_list = list_one + list_two
    
    # Initialize an empty list to store unique elements
    final_list = []
    
    # Remove duplicates from the combined list
    for element in combined_list:
        if element not in final_list:
            final_list.append(element)
    
    # Implement bubble sort to sort the list in ascending order
    for i in range(len(final_list)):
        for j in range(i+1, len(final_list)):
            if final_list[i] > final_list[j]:
                final_list[i], final_list[j] = final_list[j], final_list[i]
    
    return final_list