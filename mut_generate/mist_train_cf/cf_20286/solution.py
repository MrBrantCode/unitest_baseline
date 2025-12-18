"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts the given array of numbers in ascending order without using any built-in sorting functions or methods. The function should also handle and display an error message if the array contains any non-numeric elements. The input array can contain integers or floats, and the function should modify the original array.
"""

def entrance(arr):
    # Check if the array contains non-numeric elements
    for element in arr:
        if not isinstance(element, (int, float)):
            print("Error: Array contains non-numeric elements")
            return
    
    n = len(arr)
    # Perform bubble sort
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]