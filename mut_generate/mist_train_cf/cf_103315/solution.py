"""
QUESTION:
Write a function named `sub_array(array, num)` that takes an array and a number `num` as input and returns a new array containing all elements of the input array except for the occurrences of `num`. The function should not modify the original array.
"""

def sub_array(array, num):
    new_array = []
    for i in range(len(array)):
        if array[i] != num:
            new_array.append(array[i])
    return new_array