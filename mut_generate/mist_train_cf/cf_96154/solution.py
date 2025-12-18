"""
QUESTION:
Implement a function named `cocktail_sort` that sorts an array in ascending order using a variation of the cocktail sort algorithm. The function should take one argument: an array of integers. The function should return the sorted array along with the total number of swaps performed during the sorting process, and it should print the array after each iteration.
"""

def cocktail_sort(arr):
    swaps = 0
    n = len(arr)
    start = 0
    end = n - 1
    sorted = False

    while not sorted:
        sorted = True

        # Forward pass (like bubble sort)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                sorted = False

        # If no swaps are made in the forward pass, the array is already sorted
        if sorted:
            break

        # Decrement end index as the last element is already in its position
        end -= 1

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                sorted = False

        # Increment start index as the first element is already in its position
        start += 1

        print(f"Iteration {swaps}: {arr}")

    return arr, swaps