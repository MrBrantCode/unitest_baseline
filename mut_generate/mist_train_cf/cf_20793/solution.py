"""
QUESTION:
Write a function named `reverse_and_sum` that takes an array of up to 10^6 integers as input, reverses the array in-place, and returns the reversed array along with the sum of its elements. The integers in the array will be between -10^6 and 10^6 (inclusive). The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def reverse_and_sum(arr):
    """
    Reverses the input array in-place and returns the reversed array along with its sum.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the reversed array and its sum.
    """
    total = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        total += arr[left] + arr[right]
        left += 1
        right -= 1

    # Add the middle element if the array length is odd
    if left == right:
        total += arr[left]

    return arr, total