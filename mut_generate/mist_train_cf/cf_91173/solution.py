"""
QUESTION:
Create a function `combine_lists(list_1, list_2)` that combines the elements of two different lists into a single list in ascending order. The elements in each list are unique and in ascending order. The function should handle lists of different lengths.
"""

def combine_lists(list_1, list_2):
    """
    This function combines the elements of two different lists into a single list in ascending order.
    
    Args:
        list_1 (list): The first list of unique elements in ascending order.
        list_2 (list): The second list of unique elements in ascending order.
    
    Returns:
        list: A combined list of elements from list_1 and list_2 in ascending order.
    """
    combined_list = []
    i = 0
    j = 0
    
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            combined_list.append(list_1[i])
            i += 1
        else:
            combined_list.append(list_2[j])
            j += 1
    
    while i < len(list_1):
        combined_list.append(list_1[i])
        i += 1
    
    while j < len(list_2):
        combined_list.append(list_2[j])
        j += 1
    
    return combined_list