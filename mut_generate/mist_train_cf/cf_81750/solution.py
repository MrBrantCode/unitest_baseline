"""
QUESTION:
Write a function `sort_negatives(num_list)` that takes a list of integers as input, sorts the negative integers in ascending order, and returns the original list with the negative integers rearranged. The non-negative integers in the list should remain in their original positions. The function should handle lists containing both positive and negative integers.
"""

def sort_negatives(num_list):
    # Separate negative numbers and sort them
    sorted_negatives = sorted(x for x in num_list if x < 0)
    
    j = 0
    # Replace negative numbers with sorted negative numbers in original list
    for i in range(len(num_list)):
        if num_list[i] < 0:
            num_list[i] = sorted_negatives[j]
            j += 1
            
    return num_list