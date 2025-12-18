"""
QUESTION:
Write a function named `find_val_indices_freq` that takes a list and a value as input and returns a tuple containing the first index of the value in the list, the last index of the value in the list, and the frequency of the value in the list. If the value is not present in the list, return (-1, -1, 0). The function should be implemented without using built-in list functions except for indexing and should be case-sensitive. The list can contain both numbers and strings.
"""

def find_val_indices_freq(lst, val):
    """
    Returns a tuple containing the first index of the value in the list, 
    the last index of the value in the list, and the frequency of the value in the list.
    
    Args:
        lst (list): A list that can contain both numbers and strings.
        val: The value to be searched in the list.
    
    Returns:
        tuple: A tuple containing the first index, last index, and frequency of the value.
    """
    first_index = -1
    last_index = -1
    freq = 0
    for i in range(len(lst)):
        if lst[i] == val:
            if first_index == -1:
                first_index = i
            last_index = i
            freq += 1
    return (first_index, last_index, freq)