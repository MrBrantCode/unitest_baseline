"""
QUESTION:
Implement a function called `quicksort` that sorts a large collection of numerical values using the Quicksort algorithm. The function should take into consideration time and space complexity and should be efficient for sorting large datasets. Note that the function may not be a stable sort and may not retain the relative order of equal elements.
"""

def quicksort(arr):
    """
    Sorts a large collection of numerical values using the Quicksort algorithm.
    
    Time complexity: O(n log n) on average, O(n^2) in the worst case
    Space complexity: O(log n)
    
    :param arr: A list of numerical values
    :return: A sorted list of numerical values
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)