"""
QUESTION:
Write a function named `find_mean_of_sorted_list` that takes a list of numbers as input, sorts it in ascending order, and returns the mean of the sorted list. The function should handle the case when the input list is empty by returning an error message.
"""

def find_mean_of_sorted_list(input_list):
    # Check if list is empty
    if not input_list:
        return "Error: The provided list is empty"
    
    # Sort the list in ascending order
    sorted_list = sorted(input_list)
    
    # Calculate the mean of the sorted list
    mean = sum(sorted_list) / len(sorted_list)

    return mean