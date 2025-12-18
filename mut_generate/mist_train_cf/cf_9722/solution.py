"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in ascending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the array.
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr