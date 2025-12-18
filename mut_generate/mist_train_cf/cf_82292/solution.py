"""
QUESTION:
Implement a function named `selection_sort` that takes a list of integers as input, sorts it in ascending order using the selection sort algorithm, and returns the sorted list along with the number of swaps made during the sorting process. The function should swap two elements only when necessary (i.e., when the current element is not already the smallest in the unsorted part of the list).
"""

def selection_sort(input_list):
    """
    Sorts the input list in ascending order using the selection sort algorithm.
    
    Args:
    input_list (list): A list of integers to be sorted.
    
    Returns:
    tuple: A tuple containing the sorted list and the number of swaps made during the sorting process.
    """
    n = len(input_list)
    swap_count = 0
    
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if input_list[j] < input_list[smallest]:
                smallest = j

        if smallest != i: # swap only when necessary
            input_list[i], input_list[smallest] = input_list[smallest], input_list[i]
            swap_count += 1
      
    return input_list, swap_count