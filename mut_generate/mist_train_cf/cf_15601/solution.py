"""
QUESTION:
Design a function named 'find_median' that takes an array as input and returns the median of the array as a floating-point number with precision up to two decimal places. The function should be able to handle arrays containing both integers and floating-point numbers, and it should have a time complexity of O(n log n), where n is the length of the input array, without using any built-in median calculation functions or libraries.
"""

def find_median(arr):
    sorted_arr = sorted(arr)  
    n = len(sorted_arr)
    middle_index = n // 2
    
    if n % 2 == 0:  
        median = (sorted_arr[middle_index - 1] + sorted_arr[middle_index]) / 2
    else:  
        median = sorted_arr[middle_index]
    
    return round(median, 2)  