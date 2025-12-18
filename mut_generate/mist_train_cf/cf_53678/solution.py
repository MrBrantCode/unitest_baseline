"""
QUESTION:
Implement a function `quick_sort(array, low, high)` that sorts an array in descending order using the Quick Sort algorithm. The function should take an array of numerical elements and two indices `low` and `high` as input, and return the sorted array. The function should use a helper function `partition(array, low, high)` to partition the array around a pivot element. The `partition` function should rearrange the array such that all elements greater than or equal to the pivot are on the left of the pivot, and all elements less than the pivot are on the right. The `quick_sort` function should recursively sort the subarrays on either side of the pivot.
"""

def quick_sort(array, low, high):
    def partition(array, low, high):
        i = low - 1   
        pivot = array[high]     

        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i + 1

    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
    return array 