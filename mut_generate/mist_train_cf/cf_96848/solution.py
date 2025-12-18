"""
QUESTION:
Implement the function `remove_duplicates(arr)` that takes an array of integers as input, removes any duplicate numbers, sorts the remaining elements in descending order, and returns two arrays: the first array contains the sorted unique elements and the second array contains the count of each unique element. The solution should be implemented in a time complexity of O(nlogn) or better and should not use any built-in sorting functions or data structures.
"""

def remove_duplicates(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    unique_arr = list(count_dict.keys())

    def partition(unique_arr, low, high):
        i = low - 1
        pivot = unique_arr[high]
        for j in range(low, high):
            if unique_arr[j] >= pivot:
                i += 1
                unique_arr[i], unique_arr[j] = unique_arr[j], unique_arr[i]
        unique_arr[i + 1], unique_arr[high] = unique_arr[high], unique_arr[i + 1]
        return i + 1

    def quicksort(unique_arr, low, high):
        if low < high:
            pivot = partition(unique_arr, low, high)
            quicksort(unique_arr, low, pivot - 1)
            quicksort(unique_arr, pivot + 1, high)
    quicksort(unique_arr, 0, len(unique_arr) - 1)

    count_arr = [count_dict[num] for num in unique_arr]

    return unique_arr, count_arr