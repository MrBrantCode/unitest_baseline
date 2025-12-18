"""
QUESTION:
Write a function `process_array` that takes an array of integers as input and modifies it in place. For each even number in the array, add 10 to it. For each odd number, subtract 5 from it. The function should return the modified array.
"""

def process_array(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] += 10
        else:
            arr[i] -= 5
    return arr