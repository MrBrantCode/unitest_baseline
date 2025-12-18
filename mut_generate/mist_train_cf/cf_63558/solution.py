"""
QUESTION:
Write a function `swap_elements(a, i, j)` that swaps the elements at indices `i` and `j` in array `a` in place, if the indices are valid. The function should check if `i` and `j` are within the bounds of the array before attempting the swap. If the indices are not valid, the function should print an error message and return the original array.
"""

def swap_elements(a, i, j):
    # Check if indices are valid
    if i < len(a) and j < len(a):
        # Temporarily save the value at i
        temp = a[i]
        # Swap the value at i with value at j
        a[i] = a[j]
        # Swap the value at j with the saved value
        a[j] = temp
    else:
        # Indices are not valid, print error message
        print("Indices are not valid")
    return a