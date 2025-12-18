"""
QUESTION:
Create a function `compute_sums` that takes an array of integers as input, calculates the sum of all elements excluding the current element for each position in the array, and returns a new array with the computed sums. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def compute_sums(array):
    total_sum = sum(array)
    result = []
    for num in array:
        result.append(total_sum - num)
    return result