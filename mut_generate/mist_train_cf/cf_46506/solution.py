"""
QUESTION:
Create a function named `median` that calculates the median of a list of numbers without using the sorting method or any built-in functions. The function should handle lists with both even and odd numbers of elements, as well as lists with duplicate elements. The median of a list with an even number of elements should be the average of the two middle elements. If the list has an odd number of elements, the median is the middle element.
"""

def median(l: list):
    """
    Return median of elements in the list l without sorting it or using built-in functions.
    Handles tuples with even and odd number of elements, and duplicates.
    """
    def partition(low, high):
        pivot = l[high]
        i = low - 1
        for j in range(low, high):
            if l[j] <= pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i+1], l[high] = l[high], l[i+1]
        return i + 1

    def quickSelect(low, high, k):
        if low == high:
            return l[low]

        pivotIndex = partition(low, high)

        if k == pivotIndex:
            return l[k]
        elif k < pivotIndex:
            return quickSelect(low, pivotIndex - 1, k)
        else:
            return quickSelect(pivotIndex + 1, high, k)

    length = len(l)
    if length % 2 == 0:
        return (quickSelect(0, length - 1, length // 2 - 1) + quickSelect(0, length - 1, length // 2)) / 2
    else:
        return quickSelect(0, length - 1, length // 2)