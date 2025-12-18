"""
QUESTION:
Create a function `sub_array(array, num)` that takes an array and a number as input and returns a new array with all occurrences of the given number removed. The function should not use the `remove()` method and should not modify the original array.
"""

def sub_array(array, num):
    new_array = []
    for i in range(len(array)):
        if array[i] != num:
            new_array.append(array[i])
    return new_array