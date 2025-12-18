"""
QUESTION:
Create a function named `shared_elements` that takes two lists as input and returns a new list containing distinct elements that are present in both input lists. The returned list should be sorted in ascending order. You cannot use Python's built-in list functions to sort the result or remove duplicates.
"""

def shared_elements(list1: list, list2: list):
    # Create an empty list to store the common elements
    common_elements = []

    # Check if each element in list1 is present in list2
    for element in list1:
        if element in list2:
            # If the element is not already in the common_elements list, add it
            if element not in common_elements:
                common_elements.append(element)

    # Sort the common_elements list (without using built-in functions)
    for i in range(len(common_elements)):
        min_idx = i
        for j in range(i+1, len(common_elements)):
            if common_elements[min_idx] > common_elements[j]:
                min_idx = j
        common_elements[i], common_elements[min_idx] = common_elements[min_idx], common_elements[i]

    return common_elements