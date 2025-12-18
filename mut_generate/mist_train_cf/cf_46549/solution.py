"""
QUESTION:
Create a function named `secondMax` that takes a list of integers as input, removes duplicates, and returns the second-highest value. The function should return the second maximum value in scenarios where the input list contains negative integers and/or repeated numbers. The function should also handle the case where the list has less than two unique elements, in which case it should return a message indicating that the array does not have a second maximum value.
"""

def secondMax(arr):
    unique_arr = list(set(arr)) 
    unique_arr.sort()
    if len(unique_arr) < 2:
        return "The array doesn't have a second maximum value"
    return unique_arr[-2]