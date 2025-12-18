"""
QUESTION:
Write a function `calculate_sum(array)` that takes an array of integers as input and returns the sum of its elements. The function must handle arrays of any size, use a single loop, and not use built-in functions or libraries for calculating the sum. The function should also handle edge cases such as negative integers and arrays containing only negative integers, and should not use temporary variables to store the sum, instead directly modifying the array to store the cumulative sum at each index.
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