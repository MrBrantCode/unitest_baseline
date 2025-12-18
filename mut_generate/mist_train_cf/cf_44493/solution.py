"""
QUESTION:
Create a function `add_element(arr, element, N)` that takes a sorted array `arr`, an integer `element`, and a maximum capacity `N` as input. The function should add the `element` to the `arr` only if the array has not reached its maximum capacity `N` and the `element` is not already present in the array and is greater than the last element of the array. If the array is already at max capacity, print an error message. The function should return the potentially modified array.
"""

def add_element(arr, element, N):
    if len(arr) < N:
        if len(arr) == 0 or (element > arr[-1] and element not in arr):
            arr.append(element)
    else:
        print("Array has reached its maximum capacity")
    return arr