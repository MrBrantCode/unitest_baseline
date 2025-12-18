"""
QUESTION:
Develop a function `find_max_k_numbers(arr, k)` that takes an array `arr` and an integer `k` as input, and returns the maximum `k` numbers from the array. The function should return a list of the `k` largest numbers in descending order, and it should not modify the original array.
"""

def find_max_k_numbers(arr, k):
    """
    Returns the maximum k numbers from the array in descending order.
    
    Args:
        arr (list): Input array of integers.
        k (int): Number of maximum values to return.
    
    Returns:
        list: List of k largest numbers in descending order.
    """
    # Create a copy of the array to avoid modifying the original array
    copyArr = arr[:]
    # Sort the array in descending order
    copyArr.sort(reverse=True)
    # Return the first k elements
    return copyArr[:k]