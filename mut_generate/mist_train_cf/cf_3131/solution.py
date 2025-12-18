"""
QUESTION:
Implement a function named `bubble_sort_strings` to sort a list of strings in descending order using a bubble sort algorithm. The function should be able to handle strings containing special characters such as punctuation marks or numbers, and these special characters should be considered as part of the string and affect the sorting order. The length of each string in the list will not exceed 100 characters.
"""

def bubble_sort_strings(strings):
    """
    Sorts a list of strings in descending order using the bubble sort algorithm.

    Args:
        strings (list): A list of strings to be sorted.

    Returns:
        list: The sorted list of strings in descending order.
    """

    # Get the length of the input list
    n = len(strings)
    
    # Repeat the process until the list is sorted
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(0, n - i - 1):
            # If we find an element that is smaller than its adjacent element, then swap them
            if strings[j] < strings[j + 1]:
                # Swap values
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True
        
        # If no two elements were swapped in inner loop, the list is sorted
        if not swapped:
            break
    
    # Return the sorted list of strings
    return strings