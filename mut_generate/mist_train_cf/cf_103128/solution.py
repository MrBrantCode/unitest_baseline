"""
QUESTION:
Create a function named `reverse_list` that takes a list `arr` as an input and reverses the order of its elements using a recursive algorithm. The function should work with lists of any length, including those containing duplicate elements.
"""

def reverse_list(arr):
    if len(arr) <= 1:
        return arr
    else:
        return reverse_list(arr[1:]) + [arr[0]]