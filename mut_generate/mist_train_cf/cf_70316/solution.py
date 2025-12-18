"""
QUESTION:
Write a function `is_odd_or_even` that takes a sorted list of integers and a target number as input, performs a binary search to find the target number in the list, and returns `True` if the number is odd, `False` if the number is even, and a message or a specific value (e.g., `False`) if the number is not found in the list.
"""

def is_odd_or_even(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return arr[mid] % 2 != 0
    print("Number not found in the array")
    return False