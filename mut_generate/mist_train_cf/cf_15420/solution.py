"""
QUESTION:
Write a function called `lexicographical_sort` that takes a list of words as input, sorts them in lexicographical order, removes duplicates, and returns the result. The sorting should be case-insensitive, and the function should not use any built-in sorting functions or libraries. The time complexity should be O(nlogn) and the space complexity should be O(1).
"""

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def lexicographical_sort(words):
    words_lower = [word.lower() for word in words]
    quicksort(words_lower, 0, len(words_lower) - 1)
    return list(dict.fromkeys(words_lower))