"""
QUESTION:
Implement a function named sort_strings that takes an array of strings as input and returns the array sorted in descending order based on the sum of the ASCII values of the characters in each string. If two strings have the same sum of ASCII values, they should be sorted lexicographically. The function should have a time complexity of O(n log n) and should not use any additional data structures or libraries for sorting.
"""

def sort_strings(arr):
    def ascii_sum(string):
        return sum(ord(char) for char in string)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while ascii_sum(arr[i]) > ascii_sum(pivot) or (ascii_sum(arr[i]) == ascii_sum(pivot) and arr[i] < pivot):
                i += 1
            
            j -= 1
            while ascii_sum(arr[j]) < ascii_sum(pivot) or (ascii_sum(arr[j]) == ascii_sum(pivot) and arr[j] > pivot):
                j -= 1
            
            if i >= j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index)
            quicksort(arr, pivot_index + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return arr