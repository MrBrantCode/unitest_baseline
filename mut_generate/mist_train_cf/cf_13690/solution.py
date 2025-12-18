"""
QUESTION:
Write a function called `array_sum` that calculates the sum of the contents in a given array of positive integers without using any built-in sum function or list comprehension. The function must have a time complexity of O(n), where n is the length of the array.
"""

def array_sum(my_array):
    total = 0
    for num in my_array:
        total += num
    return total