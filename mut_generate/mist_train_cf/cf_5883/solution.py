"""
QUESTION:
Implement a function named cocktail_sort that takes an array of integers as input and sorts it in ascending order while maintaining the relative order of duplicate elements. The function should also track and print the number of swaps performed after each iteration of the sorting process.
"""

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    swaps = 0

    while swapped:
        swapped = False

        # Perform a bubble sort in the forward direction
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                swaps += 1

        # Print the intermediate sorted array
        print(f"Iteration {swaps}: {arr}")

        if not swapped:
            break

        swapped = False

        # Move the end point one step to the left
        end -= 1

        # Perform a bubble sort in the backward direction
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                swaps += 1

        # Move the start point one step to the right
        start += 1

    return arr