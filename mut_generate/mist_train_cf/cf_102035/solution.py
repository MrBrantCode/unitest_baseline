"""
QUESTION:
Remove Zero and Sort List Function

Create a function named `remove_zero_and_sort` that takes a list of integers as input, removes all elements with a value of 0, sorts the remaining elements in ascending order, and returns the sorted list. The function should not modify the original list.

Constraints:
- The length of the input list is at most 10^6.
- The values in the input list are integers in the range of -10^9 to 10^9.
- The time complexity should be O(nlogn) or better.
- The space complexity should be O(n) or better.
"""

def remove_zero_and_sort(lst):
    """
    Removes all elements with a value of 0 from the input list, 
    sorts the remaining elements in ascending order, and returns the sorted list.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new sorted list with all zeros removed.
    """
    return sorted([i for i in lst if i != 0])