"""
QUESTION:
Create a function named `sum_with_exception` that takes two parameters: an array of numbers and a threshold value. The function should return the sum of all elements in the array, but it must raise an exception with the error message "Array contains negative numbers" if the array contains any negative number, and raise a different exception with the error message "Sum exceeds threshold value" if the sum of all elements exceeds the threshold value.
"""

def sum_with_exception(arr, threshold):
    total_sum = sum(arr)
    if any(num < 0 for num in arr):
        raise Exception("Array contains negative numbers.")
    elif total_sum > threshold:
        raise Exception("Sum exceeds threshold value.")
    return total_sum