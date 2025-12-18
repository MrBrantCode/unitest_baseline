"""
QUESTION:
Write a function named `max_adjacent` that takes an array of integers as input and returns a tuple containing the starting index, ending index, and maximum number of adjacent elements in the array that are divisible by 3.
"""

def max_adjacent(arr):
    max_count = 0
    start_index = -1
    end_index = -1
    
    count = 0
    current_start = -1
    
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            count += 1
            if current_start == -1:
                current_start = i
        else:
            if count > max_count:
                max_count = count
                start_index = current_start
                end_index = i - 1
            
            count = 0
            current_start = -1
    
    if count > max_count:
        max_count = count
        start_index = current_start
        end_index = len(arr) - 1
    
    return start_index, end_index, max_count