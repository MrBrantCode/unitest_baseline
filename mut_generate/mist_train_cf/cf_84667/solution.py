"""
QUESTION:
What is the computational complexity of the given function `add_array_elements(arr)`, where `arr` is an array of integers and the function calculates the sum of all elements in the array. The function has a single loop that iterates over the array, and within the loop, it accesses each element and adds it to a running sum.
"""

def add_array_elements(arr):
    sum_elements = 0
    for i in arr:
        sum_elements += i
    return sum_elements