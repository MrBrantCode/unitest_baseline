"""
QUESTION:
Combine two lists into one sorted list in descending order without duplicates. Write a function `combine_lists` that takes two lists as input and returns a new list containing all unique elements from both input lists, sorted in descending order. Do not use built-in sorting or duplicate removal functions.
"""

def combine_lists(list_one, list_two):
    """
    Combine two lists into one sorted list in descending order without duplicates.
    
    Args:
    list_one (list): The first list of elements.
    list_two (list): The second list of elements.
    
    Returns:
    list: A new list containing all unique elements from both input lists, sorted in descending order.
    """
    
    # Combine the two lists
    combined_list = list_one + list_two
    
    # Remove duplicates
    combined_list = list(dict.fromkeys(combined_list))
    
    # Sort in descending order
    for i in range(len(combined_list)):
        for j in range(i + 1, len(combined_list)):
            if combined_list[i] < combined_list[j]:
                combined_list[i], combined_list[j] = combined_list[j], combined_list[i]
    
    return combined_list