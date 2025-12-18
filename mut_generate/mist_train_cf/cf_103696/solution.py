"""
QUESTION:
Write a function named `modify_array` that takes an array of integers as input. Iterate through the array from the last index to the first, and for each element, check if it is divisible by 2. If it is, multiply the element by 3 and add 1; otherwise, subtract 1 from the element. Return the modified array.

The input array can contain any number of integers, and the function should work for any valid input array.
"""

def modify_array(array):
    for i in range(len(array)-1, -1, -1):
        if array[i] % 2 == 0:
            array[i] = array[i] * 3 + 1
        else:
            array[i] -= 1
    return array