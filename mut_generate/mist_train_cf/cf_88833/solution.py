"""
QUESTION:
Implement a function named `quicksort` that takes a list of elements as input and returns the sorted list. The function should handle duplicate elements in the input array. The function should use the divide-and-conquer approach and partition the array into three subarrays - lesser elements, equal elements, and greater elements. The function should select a pivot element from the array and recursively apply the quicksort algorithm to the lesser and greater subarrays. The time complexity of the function should be O(n log n) in the average and best cases, and O(n^2) in the worst case.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    equal = [x for x in arr if x == pivot]
    lesser = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(lesser) + equal + quicksort(greater)