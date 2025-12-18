"""
QUESTION:
Write a function named `compute_average` that takes an array of integers as input and returns the average value of the elements in the array. The array will have a size between 1 and 10^6 (inclusive), and each integer will be between -10^9 and 10^9 (inclusive). The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def compute_average(array):
    size = len(array)
    total_sum = 0
    for num in array:
        total_sum += num
    average = total_sum / size
    return average