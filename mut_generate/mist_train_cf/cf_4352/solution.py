"""
QUESTION:
Write a function called `find_mean_median` that calculates the mean and median of a given list of positive integers. The function should be able to handle cases where the list may contain duplicates or be unsorted, and should optimize the calculation to reduce time complexity and avoid unnecessary calculations. The function should take a list of integers as input and return the mean and median as output.
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index-1, k)
    else:
        return quickselect(arr, pivot_index+1, high, k)

def find_mean_median(numbers):
    n = len(numbers)
    mean = sum(numbers) / n

    median = quickselect(numbers, 0, n-1, n//2)
    if n % 2 == 0:
        median = (median + quickselect(numbers, 0, n-1, n//2-1)) / 2

    return mean, median