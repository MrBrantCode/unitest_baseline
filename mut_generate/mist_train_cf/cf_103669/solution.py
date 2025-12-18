"""
QUESTION:
Write a function `find_largest_adjacent_sum` that takes an array of integers and a threshold value as input. The function should find the two adjacent elements in the array with the largest sum that is greater than the threshold value. If no such pair exists, it should indicate that no adjacent pair satisfies the condition.
"""

def find_largest_adjacent_sum(array, threshold):
    largest_sum = threshold
    adjacent_elements = None
    
    for i in range(1, len(array)):
        current_sum = array[i] + array[i-1]
        
        if current_sum > largest_sum and current_sum > threshold:
            largest_sum = current_sum
            adjacent_elements = (array[i-1], array[i])
    
    return adjacent_elements