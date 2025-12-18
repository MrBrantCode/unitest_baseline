"""
QUESTION:
Implement a function `sort_array(arr)` that takes an array of elements as input and sorts it in ascending order. The function should handle non-numeric elements by displaying an error message and returning without sorting the array. The sorting algorithm should have a time complexity of less than or equal to O(n^2), where n is the length of the array, and should not use any built-in sorting functions or methods.
"""

def sort_array(arr):
    def is_numeric(element):
        try:
            float(element)
            return True
        except ValueError:
            return False

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    for element in arr:
        if not is_numeric(element):
            print("Error: Array contains non-numeric elements")
            return

    bubble_sort(arr)
    return arr