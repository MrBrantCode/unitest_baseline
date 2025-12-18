"""
QUESTION:
Implement a function `mergeSort(array)` to sort a given array using the merge sort algorithm. The function should take an array as input and return the sorted array. The array may contain duplicate elements, and the function should be able to handle arrays of any size. The function should not use any built-in sorting methods.
"""

def mergeSort(array):
    if len(array) > 1:

        # Finding the mid of the array
        mid = len(array) // 2

        # Dividing the array elements
        left = array[:mid]
        right = array[mid:]

        # Sorting the first half
        mergeSort(left)

        # Sorting the second half
        mergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array