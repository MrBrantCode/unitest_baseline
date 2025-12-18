"""
QUESTION:
Write a function `is_subset_with_counts(A, B)` that determines if list B is a subset of list A, considering duplicate elements, and returns a boolean value along with a dictionary. The dictionary should contain the count of each element in B that is present in A. The function should have a time complexity of O(n), where n is the length of B.
"""

def is_subset_with_counts(A, B):
    """
    Determines if list B is a subset of list A, considering duplicate elements,
    and returns a boolean value along with a dictionary. The dictionary contains
    the count of each element in B that is present in A.

    Args:
        A (list): The superset list.
        B (list): The subset list.

    Returns:
        tuple: A boolean indicating if B is a subset of A, and a dictionary
            containing the counts of each element in B that is present in A.
    """
    count_dict = {}
    
    # Create a dictionary to store the counts of each element in A
    for element in A:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    # Check if all elements in B are present in A and update the count_dict
    for element in B:
        if element in count_dict and count_dict[element] > 0:
            count_dict[element] -= 1
        else:
            return False, {}
    
    # Create a new dictionary with the counts of each element in B that is present in A
    subset_count_dict = {element: A.count(element) - count_dict[element] for element in B}
    
    return True, subset_count_dict