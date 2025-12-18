"""
QUESTION:
Write a function `selection_sort(arr)` that sorts the input array `arr` in ascending order using the selection sort technique. The function should handle arrays containing duplicate integers and maintain a time complexity of less than O(n^2) and a space complexity of less than O(n).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] == arr[min_index] and j != min_index:
                continue  # Skip duplicate elements
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr