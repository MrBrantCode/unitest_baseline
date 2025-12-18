"""
QUESTION:
Write a function `split_array` that takes a list of integers as input, and returns a tuple containing two lists. The function should first sort the input list in ascending order, then divide it into two sublists of equal size. If the input list has an odd number of elements, the function should still divide it into two sublists of as close to equal size as possible. The function should return these two sublists in the tuple.
"""

def split_array(arr):
    sorted_arr = sorted(arr)
    middle = len(sorted_arr) // 2
    subarray1 = sorted_arr[:middle]
    subarray2 = sorted_arr[middle:]
    return subarray1, subarray2