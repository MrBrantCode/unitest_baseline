"""
QUESTION:
Calculate the disparity between the maximum and minimum numerical values in a list of lists. The function should handle empty lists or sublists, and ignore non-numerical values. If no numerical values are present, return a message indicating so.

The function, `calculate_disparity`, takes a list of lists as input and returns either the disparity between the maximum and minimum numerical values or a message if no numerical values are found.
"""

def calculate_disparity(lst):
    # Initialize a null list to store the numerical values
    num_list = []
    
    # Iterate through each sublist in the provided list
    for sublist in lst:
        # Continue to the next sublist if the current one is empty
        if not sublist:
            continue
            
        # Iterate through each item in the current sublist
        for item in sublist:
            # If the item is a number (integer or float), add it to the num_list
            if isinstance(item, (int, float)):
                num_list.append(item)
                
    # If num_list is still empty after the iteration, there were no numerical values in lst
    if not num_list:
        return "No numerical values in the list"
    
    # Calculate and return the disparity between the max and min numerical values
    return max(num_list) - min(num_list)