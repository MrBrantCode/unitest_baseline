"""
QUESTION:
Write a function `sum_unique_elements` that takes two lists of equal length, combines corresponding elements from both lists, removes duplicates, sorts the result in descending order, and returns it as a comma-separated string. The function should return an error message if the input lists have different lengths.
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