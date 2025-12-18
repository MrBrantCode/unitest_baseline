"""
QUESTION:
Create a function named 'greater_than' that takes an array of integers and a number as input, and returns a new array containing elements from the input array that are greater than the given number.
"""

def greater_than(arr, num):
    new_arr = []
    for i in arr:
        if i > num:
            new_arr.append(i)
    return new_arr