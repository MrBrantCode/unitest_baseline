"""
QUESTION:
Write a function `compute_sum_array(arr)` that takes an array of integers and returns an array of the same size. Each element in the returned array should be equal to the sum of all the elements in the original array except itself. If the sum of all the elements in the original array except the current element is negative, the corresponding element in the result array should be set to 0. If the sum of all the elements in the original array except the current element is zero, the corresponding element in the result array should be set to 1. The function should not modify the input array and should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.
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