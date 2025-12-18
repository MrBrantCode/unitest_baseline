"""
QUESTION:
Write a function called `move_to_end` that takes an array and a specific value as input, and moves all elements of that value to the end of the array in-place without preserving their relative order. The function should modify the original array and return it. The array can contain duplicate elements and the function should work for any type of elements in the array.
"""

def move_to_end(array, to_move):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == to_move:
            j -= 1
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array