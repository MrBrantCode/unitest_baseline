"""
QUESTION:
Given an array of integers and a limit for distinct element changes, write a function `smallest_change(arr, limit)` that returns the minimum number of elements that need to be changed within the given limit to make the array palindromic. If the array cannot be made palindromic within the given limit, return -1.
"""

def smallest_change(arr, limit):
    """
    Returns the minimum number of elements that need to be changed within the given limit to make the array palindromic.
    If the array cannot be made palindromic within the given limit, return -1.

    :param arr: The input array of integers
    :type arr: list
    :param limit: The limit for distinct element changes
    :type limit: int
    :return: The minimum number of elements that need to be changed, or -1 if not possible
    :rtype: int
    """
    def count_changes(i, j, memo):
        if i >= j:
            return 0
        if (i, j, limit) in memo:
            return memo[(i, j, limit)]
        
        if arr[i] == arr[j]:
            count = count_changes(i + 1, j - 1, memo)
        else:
            count = 1 + count_changes(i + 1, j - 1, memo)
        
        memo[(i, j, limit)] = count
        return count
    
    memo = {}
    changes = count_changes(0, len(arr) - 1, memo)
    
    if changes <= limit * 2:
        return changes // 2
    else:
        return -1