"""
QUESTION:
Implement a function named `selection_sort` that takes two parameters: a list of integers `arr` and an optional parameter `order` with a default value of `'asc'`. The function should sort the list in ascending order if `order` is `'asc'`, and in descending order if `order` is `'desc'`. The function should return the sorted list.
"""

def selection_sort(arr, order='asc'):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if order == 'desc':
                if arr[j] > arr[index]:
                    index = j
            else:
                if arr[j] < arr[index]:
                    index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr