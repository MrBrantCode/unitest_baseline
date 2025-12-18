"""
QUESTION:
Write a function called 'median' to calculate the median of an array of integers. The median is the middle value of a sorted array. If the array has an odd number of elements, the median is the middle element. If the array has an even number of elements, the median is the average of the two middle elements. You cannot use any loops or recursion in your solution, and you are not allowed to use any built-in functions for sorting the array. The input array will always have at least one element and may contain duplicate elements.
"""

def median(array):
    def quicksort(array):
        if len(array) <= 1:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    sorted_array = quicksort(array)
    length = len(sorted_array)
    if length % 2 == 1:
        return sorted_array[length // 2]
    else:
        return (sorted_array[length // 2 - 1] + sorted_array[length // 2]) / 2