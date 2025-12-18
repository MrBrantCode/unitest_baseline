"""
QUESTION:
Write a function `find_first_negative(arr)` that finds the first negative number in each sub-array of a multidimensional array `arr`. The function should return a list of the first negative numbers found in each sub-array, or `None` if no negative number is found. The input `arr` is a multidimensional array of integers.
"""

def find_first_negative(arr):
    result = []
    for sub_arr in arr:
        found = False
        for num in sub_arr:
            if num < 0:
                result.append(num)
                found = True
                break
        if not found:
            result.append(None)
    return result