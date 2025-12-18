"""
QUESTION:
Write a function named `reverse_double` that takes a list of integers `arr` as input, where 2 <= len(arr) <= 1000 and -1000 <= arr[i] <= 1000 for all i, with no duplicate integers. The function should return a new list of integers where each element from the input list is repeated twice, sorted in ascending order, and the order of the repeated elements is reversed compared to the original list. The time complexity should be O(n log n) and the space complexity should be O(n).
"""

def reverse_double(arr):
    """
    This function takes a list of integers, repeats each element twice, 
    sorts them in ascending order, and reverses the order of the repeated elements.

    Parameters:
    arr (list): A list of integers with no duplicates.

    Returns:
    list: A new list of integers with each element from the input list repeated twice, 
          sorted in ascending order, and the order of the repeated elements reversed.
    """
    result = []
    for num in sorted(arr):
        result.extend([num, num])
    return result[::-1]