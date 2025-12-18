"""
QUESTION:
Implement a function called `insertion_sort` that sorts an array of integers in ascending order. The function should take one parameter, `arr`, which is a list of integers. The function should return the sorted array. The function should have a time complexity of O(n^2) and should work by dividing the array into a sorted and an unsorted region, inserting each element from the unsorted region into its correct position in the sorted region.
"""

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr