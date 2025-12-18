"""
QUESTION:
Write a function named `calculate_sum` that takes an array of integers as input, calculates the cumulative sum at each index by modifying the array in-place, and returns the final sum. The function should handle arrays of any size (0 to 10^6 elements), including edge cases with negative integers and arrays containing only negative integers. The function should only use a single loop to iterate through the array and should not use any built-in functions or libraries for calculating the sum.
"""

def calculate_sum(array):
    if len(array) == 0:  
        return 0
    elif len(array) == 1:  
        return array[0]
    else:
        if array[0] < 0:  
            array[0] = 0
        for i in range(1, len(array)):
            if array[i] < 0:
                array[i] = array[i-1]  
            array[i] += array[i-1]  
        return array[-1]  