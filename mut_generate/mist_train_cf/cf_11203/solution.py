"""
QUESTION:
Write a function `merge_and_sort_lists` that takes two lists of integers as input: a main list and a list of prime numbers in descending order. The function should merge the two lists, remove any duplicates, and return the resulting list in ascending order, without modifying the original lists. The list of prime numbers may contain duplicate values.
"""

def merge_and_sort_lists(main_list, prime_numbers):
    """
    Merge two lists of integers, remove duplicates, and return the resulting list in ascending order.

    Args:
        main_list (list): The main list of integers.
        prime_numbers (list): A list of prime numbers in descending order.

    Returns:
        list: The merged list in ascending order without duplicates.
    """
    # Merge the two lists
    merged_list = main_list + prime_numbers
    
    # Remove duplicates by converting to a set and then back to a list
    merged_list = list(set(merged_list))
    
    # Sort the list in ascending order
    merged_list.sort()
    
    return merged_list