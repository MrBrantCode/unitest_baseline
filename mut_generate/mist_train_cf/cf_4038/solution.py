"""
QUESTION:
Implement a function `sort_strings(arr)` that sorts an array of strings `arr` in-place in descending order based on the number of vowels in each string. The function should correctly handle strings with uppercase letters, special characters, and duplicate strings, maintaining the original order of duplicates. The function should use O(1) extra space and have a time complexity of O(n log n).
"""

def sort_strings(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        
        for j in range(low, high):
            if count_vowels(arr[j]) >= count_vowels(pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def count_vowels(string):
        vowels = set('aeiouAEIOU')
        count = 0
        for char in string:
            if char in vowels:
                count += 1
        return count

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    quicksort(arr, 0, len(arr) - 1)