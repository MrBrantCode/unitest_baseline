"""
QUESTION:
Write a function named `remove_duplicates` that takes an array as input and returns a new array containing only the unique elements from the input array. The function should not use any built-in methods or data structures (such as sets or dictionaries) to store unique values and should be able to handle arrays containing non-integer values, including strings and objects.
"""

def remove_duplicates(arr):
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    return unique_arr