"""
QUESTION:
Write a function `sum_unique_elements` that takes two lists of integers, `list1` and `list2`, with the same length. The function should create a new list by adding corresponding elements from both lists, remove duplicates, sort the list in descending order, and return the result as a comma-separated string. If the input lists are not of the same length, the function should return an error message.
"""

def sum_unique_elements(list1, list2):
    # Check if the lists have the same length
    if len(list1) != len(list2):
        return "Error: The lists should have the same length"
    
    # Create a new list by taking the elements at the same index from both lists
    new_list = [list1[i] + list2[i] for i in range(len(list1))]
    
    # Remove duplicate elements
    unique_list = list(set(new_list))
    
    # Sort the unique list in descending order
    unique_list.sort(reverse=True)
    
    # Convert the sorted list to a string with elements separated by a comma
    result = ",".join(str(element) for element in unique_list)
    
    return result