"""
QUESTION:
Implement a function `find_median` that calculates the median of a list of positive integers using only logical operations, bitwise operators, and recursion. The function must have a time complexity of O(n log n), where n is the length of the list. The median is the middle value of a sorted list of numbers; for an odd-length list, it is the middle number, and for an even-length list, it is the average of the two middle numbers.
"""

def find_median(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        middle_right = len(arr) // 2
        middle_left = middle_right - 1
        return (arr[middle_left] + arr[middle_right]) // 2