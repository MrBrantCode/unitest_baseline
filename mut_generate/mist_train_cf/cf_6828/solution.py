"""
QUESTION:
Implement the `cocktail_shaker_sort` function that sorts a given list of integers using the cocktail shaker sort algorithm. The function should return the sorted list and the total number of swaps made during the sorting process. The optimized version should reduce the time complexity to O(n^2/2), where n is the size of the input list, by breaking the loop early if no swaps are made in a pass. The space complexity of the algorithm should be O(1).
"""

def cocktail_shaker_sort(arr):
    n = len(arr)
    swaps = 0
    left = 0
    right = n - 1

    while left < right:
        swapped = False

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1

        if not swapped:
            break

        right -= 1

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                swaps += 1

        if not swapped:
            break

        left += 1

    return arr, swaps