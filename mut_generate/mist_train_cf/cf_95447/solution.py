"""
QUESTION:
Write a function named `reverse_slice` that takes a list and an integer index as input, reverses the list up to the given index, and returns the reversed slice without using any built-in list manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the list.
"""

def reverse_slice(lst, index):
    start_index = 0
    end_index = index

    while start_index < end_index:
        # Swap the elements at start_index and end_index
        temp = lst[start_index]
        lst[start_index] = lst[end_index]
        lst[end_index] = temp
        
        # Move to the next elements
        start_index += 1
        end_index -= 1

    return lst[:index + 1]