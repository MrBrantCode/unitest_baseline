"""
QUESTION:
Create a function `cumulative_sum(array)` that calculates the cumulative sum of the input array, excluding the first two elements. The function should return a list where the first two elements are 0, and the rest of the elements are the cumulative sum of the corresponding elements in the input array. The input array should have at least 3 elements.
"""

def cumulative_sum(array):
    if len(array) < 3:
        return "Array should have at least 3 elements"
    
    cumulative_sum = [0] * len(array)
    cumulative_sum[2] = array[2]

    for i in range(3, len(array)):
        cumulative_sum[i] = cumulative_sum[i-1] + array[i]

    return cumulative_sum