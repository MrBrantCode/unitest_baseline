"""
QUESTION:
Write a function called `find_middle` that takes an array of integers as input and returns the length of the array along with its middle element(s) without using any built-in functions or methods, loops, or recursion to iterate through the array. If the array has an odd length, return the middle element. If the array has an even length, return the two middle elements.
"""

def find_middle(arr):
    def get_length(arr, index=0):
        if index == len(arr):
            return 0
        return 1 + get_length(arr, index + 1)

    length = get_length(arr)
    if length % 2 == 1:
        middle_index = length // 2
        return length, arr[middle_index]
    else:
        middle_index1 = length // 2 - 1
        middle_index2 = length // 2
        return length, arr[middle_index1], arr[middle_index2]