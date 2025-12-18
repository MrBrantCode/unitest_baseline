"""
QUESTION:
Write a function `find_first_repeating(arr)` that finds the first repeating element in a given array of integers. If no repeating element is found, return -1. The function should only return the first repeating element it encounters in the array. The array can contain duplicate values and the function should have a time complexity of O(n).
"""

def find_first_repeating(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in arr:
        if count_dict[num] > 1:
            return num

    return -1