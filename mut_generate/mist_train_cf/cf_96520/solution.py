"""
QUESTION:
Write a function `find_adjacent_elements` that takes an array of integers and a threshold value as input, and returns the two adjacent elements in the array with the largest sum that is greater than the threshold value. The two adjacent elements must not be located at the beginning or end of the array. If no such pair exists, return None.
"""

def find_adjacent_elements(array, threshold):
    max_sum = float('-inf')
    max_sum_index = -1

    # Iterate through the array, excluding the first and last elements
    for i in range(1, len(array) - 1):
        # Calculate the sum of the adjacent elements
        current_sum = array[i] + array[i+1]
        
        # Check if the sum is greater than the threshold and the current sum is larger than the previous max sum
        if current_sum > threshold and current_sum > max_sum:
            max_sum = current_sum
            max_sum_index = i

    if max_sum_index != -1:
        return [array[max_sum_index], array[max_sum_index+1]]
    else:
        return None