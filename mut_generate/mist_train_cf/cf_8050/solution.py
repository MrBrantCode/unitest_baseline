"""
QUESTION:
Write a function named `compute_sum_array` that takes an array of integers and returns an array of the same size with each element equal to the sum of all the elements in the original array except itself. If the sum of all the elements except the current element is negative, set the corresponding element in the result array to 0. If the sum of all the elements except the current element is zero, set the corresponding element in the result array to 1. The function should not modify the input array and should meet the following constraints: time complexity O(n), space complexity O(1), where n is the length of the input array.
"""

def compute_sum_array(arr):
    total_sum = sum(arr)
    n = len(arr)
    sum_array = [0] * n

    for i in range(n):
        sum_except_current = total_sum - arr[i]
        if sum_except_current < 0:
            sum_array[i] = 0
        elif sum_except_current == 0:
            sum_array[i] = 1
        else:
            sum_array[i] = sum_except_current

    return sum_array