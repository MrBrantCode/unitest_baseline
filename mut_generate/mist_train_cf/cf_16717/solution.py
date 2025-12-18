"""
QUESTION:
Implement the `quicksort` function to sort an array of strings in ascending order. The input array will contain strings of lowercase letters with a maximum length of 100 characters and a maximum array length of 1,000,000. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def quicksort(arr):
    """
    Sorts an array of strings in ascending order using the quicksort algorithm.

    Time complexity: O(n log n)
    Space complexity: O(log n)

    Args:
        arr (list): The input array of strings.

    Returns:
        list: The sorted array of strings.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)