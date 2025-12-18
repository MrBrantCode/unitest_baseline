"""
QUESTION:
Implement the `Sort` function that takes a list of integers as input and returns the sorted list. The function should sort the input list in ascending order using a simple sorting algorithm. The function should not use any built-in sorting methods and should only modify the original list by swapping elements.
"""

def sort(input_list):
    """
    Sorts a list of integers in ascending order using a simple sorting algorithm.

    Args:
        input_list (list): The list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """

    # Loop through the list 
    for i in range(len(input_list) - 1):
      
        # Initialize the current minimum index
        current_min_index = i 

        # Search for the lowest element
        for j in range(i + 1, len(input_list)):
            # Update the smallest element
            if input_list[j] < input_list[current_min_index]:
                current_min_index = j
        
        # Swap the smallest element
        if current_min_index != i:
            input_list[current_min_index], input_list[i] = input_list[i], input_list[current_min_index]
    
    # Return the sorted list
    return input_list