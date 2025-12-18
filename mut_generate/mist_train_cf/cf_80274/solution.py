"""
QUESTION:
Implement a function named `cocktail_sort` that takes a list of integers as input and returns the sorted list using the bidirectional Bubble Sort (Cocktail Sort) algorithm. Optimize the algorithm by keeping track of the last swapped indices in both directions to skip unnecessary iterations.
"""

def cocktail_sort(arr):
    n = len(arr)
    last_swap_left = 0
    last_swap_right = n - 1

    while last_swap_left < last_swap_right:
        right_swap = last_swap_left
        left_swap = last_swap_right

        for i in range(last_swap_left, last_swap_right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                right_swap = i

        last_swap_right = right_swap

        for i in range(last_swap_right, last_swap_left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                left_swap = i

        last_swap_left = left_swap

    return arr