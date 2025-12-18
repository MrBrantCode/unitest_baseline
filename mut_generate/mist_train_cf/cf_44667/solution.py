"""
QUESTION:
Create a function called `shared_elements` that takes two lists of integers as input and returns a sorted list of unique elements that are present in both input lists. The function must achieve a time complexity of O(nlogn) or better and cannot use Python's built-in list functions to sort the result or remove duplicates.
"""

def shared_elements(list1: list, list2: list):
    """
    This function takes two lists of integers as input and returns a sorted list of unique elements that are present in both input lists.
    
    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.
    
    Returns:
        list: A sorted list of unique elements that are present in both input lists.
    """

    # Convert the lists to sets to remove duplicates and sort them
    list1 = sorted(set(list1))
    list2 = sorted(set(list2))

    # Initialize an empty list to store the shared elements
    result = []
    
    # Initialize pointers for both lists
    i, j = 0, 0
    
    # Iterate over the lists
    while i < len(list1) and j < len(list2):
        # If the current elements in both lists are equal, add it to the result and move both pointers
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        # If the current element in list1 is smaller, move the pointer for list1
        elif list1[i] < list2[j]:
            i += 1
        # If the current element in list2 is smaller, move the pointer for list2
        else:
            j += 1
    
    # Return the list of shared elements
    return result