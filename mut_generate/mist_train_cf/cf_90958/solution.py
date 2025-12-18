"""
QUESTION:
Implement a function `gnome_sort` that takes an array as input and sorts it in ascending order using the Gnome sort algorithm. The function must use only a constant amount of extra space and have a time complexity of O(n^2), where n is the size of the array.
"""

def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index += 1
        elif arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr