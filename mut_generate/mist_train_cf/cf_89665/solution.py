"""
QUESTION:
Implement a recursive Gnome sort function in Python, `gnome_sort(arr, i=0)`, that sorts the input list of strings in lexicographic order. The function should not use any built-in sorting functions or libraries and should recursively swap adjacent elements if they are in the wrong order until the entire list is sorted.
"""

def gnome_sort(arr, i=0):
    if i == 0:
        i = 1
    
    if i >= len(arr):
        return arr
    
    if arr[i] >= arr[i-1]:
        return gnome_sort(arr, i+1)
    else:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        return gnome_sort(arr, i-1)