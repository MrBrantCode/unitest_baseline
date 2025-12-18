"""
QUESTION:
Write a function `findZeros` that takes an array of integers as input and returns a list of indices where the value of the element in the array is 0.

The input array is of length n (1 <= n <= 10^6) and contains integers between -1000 and 1000. The time complexity of the solution should be O(n), but due to the nature of the problem, the space complexity cannot be O(1) as it is not possible to store the indices without using extra space.
"""

def find_zeros(arr):
    """
    This function finds the indices of zeros in a given array.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of indices where the value of the element in the array is 0.
    """
    return [i for i, num in enumerate(arr) if num == 0]