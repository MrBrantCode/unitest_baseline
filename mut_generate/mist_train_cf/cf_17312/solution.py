"""
QUESTION:
Write a function named `compare_lists` that takes two lists as input. Compare the input list with a pre-defined list in a case-insensitive manner and return a new list containing only the elements that are present in both lists. Ensure the resulting list does not contain any duplicate elements and maintains the original case of the elements from the input list.
"""

def compare_lists(my_list, pre_defined_list):
    # Convert both lists to lowercase
    my_list_lower = [element.lower() for element in my_list]
    pre_defined_list_lower = [element.lower() for element in pre_defined_list]
    
    # Find the common elements between the two lists
    common_elements = list(set(my_list_lower) & set(pre_defined_list_lower))
    
    # Remove any duplicate elements from the resulting list
    unique_elements = list(set(common_elements))
    
    # Convert the elements back to their original case
    result = [element for element in my_list if element.lower() in unique_elements]
    
    return result