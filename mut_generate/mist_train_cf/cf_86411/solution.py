"""
QUESTION:
Write a function `find_largest_number` that finds the largest number in a given array and returns the number along with its corresponding index. If multiple numbers have the same maximum value, return the index of the first occurrence. The function should have a time complexity of O(n) and use only a single loop to iterate through the array without using any built-in array sorting or searching functions. The array may contain positive and negative integers.
"""

def find_largest_number(arr):
    largest_num = arr[0]
    largest_index = 0
    for i in range(len(arr)):
        if arr[i] > largest_num:
            largest_num = arr[i]
            largest_index = i
    return largest_num, largest_index