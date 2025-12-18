"""
QUESTION:
Create a function named `custom_sort(arr)` that sorts a given 2D array `arr` in ascending order based on the second element of each array element pair. If two elements have the same second element, sort them based on the first element in descending order. Additionally, if two elements have the same second element and first element, sort them based on the sum of the third and fourth elements in ascending order. The array size will be at most 10^6 and the values of the elements will be between -10^9 and 10^9.
"""

def custom_sort(arr):
    arr.sort(key=lambda x: (x[1], -x[0], x[2] + x[3]))
    return arr