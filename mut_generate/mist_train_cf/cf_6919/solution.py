"""
QUESTION:
Implement the gnome_sort function in Python, which sorts a list of strings in lexicographic order using a recursive approach. The function should not use any built-in sorting functions or libraries. The gnome_sort function should take a list of strings as input and return the sorted list.
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