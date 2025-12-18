"""
QUESTION:
Implement a function `sort_multidimensional_array` that sorts the elements of a given multidimensional array in ascending order from left to right and then top to bottom. The array is sorted in a way that the first row is filled first, then the second row, and so on. If two elements have equal values, their original order should be preserved. The input array is a list of lists where each inner list has the same length.
"""

def sort_multidimensional_array(mat):
    flattened_arr = [item for sublist in mat for item in sublist]
    sorted_arr = sorted(flattened_arr)
    return [sorted_arr[i:i+len(mat[0])] for i in range(0, len(sorted_arr), len(mat[0]))]