"""
QUESTION:
Write a function named `get_products` that takes an array of numbers as input and returns an array whose elements are the product of all the elements in the input array except the element at the current index. The input array will contain at least one element.
"""

def get_products(arr):
    """
    Returns an array whose elements are the product of all the elements in the input array except the element at the current index.

    Args:
        arr (list): An array of numbers.

    Returns:
        list: An array of products.
    """
    left = [1]
    right = [1]
    ans = []

    # Traverse from left to right
    for i in range(1, len(arr)):
        left.append(arr[i-1] * left[i-1])

    # Traverse from right to left
    for i in reversed(range(len(arr)-1)):
        right.insert(0, arr[i+1] * right[0])

    # Compute the product of all elements except itself
    for i in range(len(arr)):
        ans.append(left[i] * right[i])

    return ans