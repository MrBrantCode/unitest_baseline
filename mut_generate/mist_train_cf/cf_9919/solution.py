"""
QUESTION:
Write a function `compute_average` that takes an array of integers as input and returns the average value of all elements in the array. The array size can range from 1 to 10^6 and each integer can be between -10^9 and 10^9 inclusive. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def compute_average(array):
    size = len(array)
    total_sum = 0
    for num in array:
        total_sum += num
    average = total_sum / size
    return average