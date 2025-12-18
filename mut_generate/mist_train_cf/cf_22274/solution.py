"""
QUESTION:
Create a function called "rearrange_array" that takes an array of integers as input, rearranges the array so that all elements divisible by 3 are first while maintaining their original relative order, followed by the remaining elements also in their original relative order, and returns the rearranged array.
"""

def rearrange_array(array):
    result = []
    for num in array:
        if num % 3 == 0:
            result.append(num)
    for num in array:
        if num % 3 != 0:
            result.append(num)
    return result