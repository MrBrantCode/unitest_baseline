"""
QUESTION:
Create a function `combine_lists(list1, list2)` that takes two lists of integers as input and returns a new list where each element is the sum of the corresponding elements in the input lists. The function should return an error message if the input lists contain non-integer elements or have different lengths.
"""

def combine_lists(list1, list2):
    # Validate input lists
    if not all(isinstance(num, int) for num in list1):
        return "Error: The first list contains non-integer element(s)."
    if not all(isinstance(num, int) for num in list2):
        return "Error: The second list contains non-integer element(s)."
    if len(list1) != len(list2):
        return "Error: The input lists have different lengths."
    
    # Combine the lists
    combined_list = [x + y for x, y in zip(list1, list2)]
    return combined_list