"""
QUESTION:
Write a function named `find_single_element` that takes an array of integers as input and returns the index of the element that occurs only once. The array contains duplicate elements, with one element appearing only once. The function should use the XOR operation and iteration, without using loops or recursion in the traditional sense, and without using any built-in functions or libraries. The input array is guaranteed to have at least one element, and the unique element is guaranteed to exist.
"""

def find_single_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return arr.index(result)