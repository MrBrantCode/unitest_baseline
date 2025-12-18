"""
QUESTION:
Write a function `calculate_statistics` that takes a list of integers as input and returns the mean, median, and mode of the list. The function should first sort the list in ascending order without using any built-in sorting functions, and then calculate the mean, median, and mode. If there are multiple modes, return all of them. If all elements in the list are unique, return 'No mode found'.
"""

def calculate_statistics(arr):
    # Sort the array in ascending order without using any built-in sorting functions
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Calculate the mean
    mean = sum(arr) / len(arr)

    # Calculate the median
    n = len(arr)
    median = (arr[n//2] if n % 2 == 1 else (arr[n//2 - 1] + arr[n//2]) / 2)

    # Calculate the mode
    from collections import Counter
    data = Counter(arr)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        mode = 'No mode found'
    else:
        mode = 'Mode is / are: ' + ', '.join(map(str, mode))

    return mean, median, mode