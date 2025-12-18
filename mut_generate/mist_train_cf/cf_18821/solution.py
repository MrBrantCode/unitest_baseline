"""
QUESTION:
Implement a function named `quickSort(arr)` to sort the given array of strings in-place in descending order based on the number of vowels in each string. The function should have a time complexity of O(n log n) and a space complexity of O(1), handling strings with uppercase letters and special characters correctly.
"""

def countVowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def partition(arr, low, high):
    pivot = countVowels(arr[high])
    i = low - 1
    for j in range(low, high):
        if countVowels(arr[j]) >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

def entrance(arr):
    n = len(arr)
    quickSort(arr, 0, n - 1)
    return arr