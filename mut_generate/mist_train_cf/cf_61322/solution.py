"""
QUESTION:
Create a function `list_compare` that takes two lists of integers as input. The function should return two lists: the first list containing integers that are present in the first input list but not in the second, and the second list containing integers that are present in both input lists. Additionally, the function should return two counters, one for each of the returned lists, representing the number of even integers in each list. Ensure the function works efficiently even with large lists.
"""

def list_compare(list1, list2):
    """
    This function compares two lists of integers.
    
    It returns two lists: the first list containing integers that are present in the first input list but not in the second,
    and the second list containing integers that are present in both input lists.
    
    Additionally, the function returns two counters, one for each of the returned lists, representing the number of even integers in each list.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        tuple: A tuple containing two lists and two counters.
    """

    # Convert the lists to sets for efficient set operations
    set1 = set(list1)
    set2 = set(list2)

    # Find the difference between the two sets
    in_first_not_second = list(set1 - set2)
    
    # Find the intersection of the two sets
    in_both = list(set1 & set2)

    # Count the number of even numbers in each list
    in_first_not_second_even = sum(1 for num in in_first_not_second if num % 2 == 0)
    in_both_even = sum(1 for num in in_both if num % 2 == 0)

    return in_first_not_second, in_both, in_first_not_second_even, in_both_even