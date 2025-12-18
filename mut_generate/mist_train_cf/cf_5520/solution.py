"""
QUESTION:
Implement a function `find_max_min_sum_average` that takes an array of integers as input, and returns the maximum, minimum, sum, and average of the elements in the array. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1). The function should not use any built-in sorting or mathematical functions, except for division to calculate the average. The input array can contain both positive and negative integers, and may have duplicate elements. The length of the array is between 1 and 10^6, and the values of the elements are between -10^6 and 10^6.
"""

def find_max_min_sum_average(arr):
    maximum = arr[0]
    minimum = arr[0]
    total_sum = 0
    
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
        total_sum += num
    
    average = total_sum / len(arr)
    
    return maximum, minimum, total_sum, average