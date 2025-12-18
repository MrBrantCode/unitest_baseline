"""
QUESTION:
Write a function `find_int` that accepts a jagged 2D array and an integer. It should return a sorted list of tuples, where each tuple contains the row and index of the integer in the array, with both the rows and indices sorted in ascending order. The function should handle arbitrary and large data sizes, including duplicate integers within the same row.
"""

def find_int(arr, num):
    coords = sorted([(i, j) for i, sub_arr in enumerate(arr) for j, elem in enumerate(sub_arr) if elem == num])
    return coords