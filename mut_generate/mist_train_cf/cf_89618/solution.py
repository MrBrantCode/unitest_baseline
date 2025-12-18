"""
QUESTION:
Implement a function called `cocktail_shaker_sort` that sorts a list of integers using the cocktail shaker sort algorithm. The function should return the sorted list and the total number of swaps made during the sorting process. Optimize the function to have an average and worst-case time complexity of O(n^2/2) and a space complexity of O(1), where n is the size of the input list.
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