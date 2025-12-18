"""
QUESTION:
Implement a function `gnome_sort` that sorts an array in ascending order using the Gnome sort algorithm, with a time complexity of O(n^2) and using only a constant amount of extra space.
"""

def gnome_sort(array):
    index = 0
    while index < len(array):
        if index == 0:
            index += 1
        elif array[index] >= array[index - 1]:
            index += 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
    return array