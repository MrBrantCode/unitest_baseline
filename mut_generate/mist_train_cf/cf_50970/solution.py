"""
QUESTION:
Implement a function `third_largest(arr)` that finds the 3rd largest number in a given array of non-repeating integers without using any inbuilt sorting function. The array contains at least three distinct integers.
"""

def third_largest(arr):
    # Implement bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j+1]:
                # Swap positions
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return third largest number
    return arr[2]