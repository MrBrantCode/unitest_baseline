"""
QUESTION:
Write a function named `custom_sort` that takes a 2D array as input where each element is a list or tuple of four integers. The function should sort the array in ascending order based on the second element of each sub-array. If two elements have the same second element, they should be sorted based on the first element in descending order. If two elements have the same second element and first element, they should be sorted based on the sum of the third and fourth elements in ascending order. The input array size will not exceed 10^6 and the values of the elements will be between -10^9 and 10^9. The function should return the sorted array.
"""

def custom_sort(arr):
    arr.sort(key=lambda x: (x[1], -x[0], x[2] + x[3]))
    return arr