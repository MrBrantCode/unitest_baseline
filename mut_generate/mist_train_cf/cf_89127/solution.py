"""
QUESTION:
Implement a recursive function `count_elements_recursive` to count the number of elements in a one-dimensional array of positive integers that are divisible by `k`, have a remainder of 1 when divided by `m`, and are greater than or equal to `n`. The function should return the total count of such elements.
"""

def count_elements_recursive(arr, k, m, n):
    """
    Recursively counts the number of elements in a one-dimensional array of positive integers 
    that are divisible by k, have a remainder of 1 when divided by m, and are greater than or equal to n.

    Args:
        arr (list): A one-dimensional array of positive integers.
        k (int): The divisor.
        m (int): The number to check for remainder.
        n (int): The minimum value.

    Returns:
        int: The total count of elements that satisfy the conditions.
    """
    if len(arr) == 0:
        return 0
    
    count = 0
    if arr[0] % k == 0 and arr[0] % m == 1 and arr[0] >= n:
        count += 1
    
    return count + count_elements_recursive(arr[1:], k, m, n)