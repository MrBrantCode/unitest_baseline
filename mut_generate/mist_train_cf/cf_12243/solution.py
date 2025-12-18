"""
QUESTION:
Write a function `longest_increasing_sequence(arr)` that takes an array of numbers as input and returns the longest increasing subsequence. The function must use a single loop and should return the subsequence, not just its length. The subsequence is considered increasing if each element is greater than its previous element.
"""

def longest_increasing_sequence(arr):
    max_length = 0
    current_length = 1
    start_index = 0
    max_start_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 1
            start_index = i
        
    if current_length > max_length:
        max_length = current_length
        max_start_index = start_index
    
    return arr[max_start_index : max_start_index + max_length]