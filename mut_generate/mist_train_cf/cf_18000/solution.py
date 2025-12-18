"""
QUESTION:
Write a function `is_palindrome(arr)` that determines if a given array is a palindrome. The array can contain both integers and strings. The function should ignore non-alphanumeric characters and case sensitivity. If the array has an odd length, the middle element can be any value. If the array has an even length, all elements must be the same value. The function should return True if the array is a palindrome and False otherwise.
"""

def is_palindrome(arr):
    # Convert all elements to lowercase strings
    arr = [str(x).lower() for x in arr]

    # Remove non-alphanumeric characters
    arr = [x for x in arr if x.isalnum()]

    # Check if the array is empty or has only one element
    if len(arr) == 0 or len(arr) == 1:
        return True

    # Check if the array has odd length
    if len(arr) % 2 != 0:
        # Find the middle index
        mid = len(arr) // 2
        # Create two subarrays: one from the beginning to the middle, and one from the middle+1 to the end
        subarray1 = arr[:mid]
        subarray2 = arr[mid+1:]
    else:
        # Check if all elements are the same
        if all(x == arr[0] for x in arr):
            return True
        else:
            return False

    # Check if the subarrays are equal when reversed
    return subarray1 == subarray2[::-1]