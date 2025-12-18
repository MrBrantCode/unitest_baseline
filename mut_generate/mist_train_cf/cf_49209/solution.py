"""
QUESTION:
Develop a function `nested_multiple_lists_sum` that calculates the cumulative total of elements within multiple lists of numerical arrays, following a specific ordering pattern. The function should take two parameters: a list of numerical arrays `list_of_lists` and an ordering list `order`, where each element in `order` represents the index of the corresponding list in `list_of_lists` (1-indexed). The function should handle any number of lists and report errors if non-numerical elements are included in the arrays or if the order is invalid.
"""

def nested_multiple_lists_sum(list_of_lists, order):
    # Initiate sum variable
    total = 0
    
    # Order checking
    if max(order) > len(list_of_lists):
        return 'Error: Invalid order.'
            
    try:
        for index in order:
            total += sum(list_of_lists[index-1])
    except TypeError as e:
        # If it encounters non-numerical element
        return 'Error: Non-numerical element found in the arrays.'
            
    return total