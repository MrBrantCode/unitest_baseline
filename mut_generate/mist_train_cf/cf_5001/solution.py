"""
QUESTION:
Write a function called `count_occurrences` that takes two parameters, `arr` and `value`, where `arr` is an array of integers and `value` is an integer. The function should return the number of occurrences of the `value` in the `arr`. The time complexity of the function should be O(n log n) and the space complexity should be O(n).
"""

def count_occurrences(arr, value):
    count = 0
    sorted_arr = sorted(arr)  # O(n log n) time complexity
    
    # Binary search for the first occurrence
    low = 0
    high = len(sorted_arr) - 1
    first_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] < value:
            low = mid + 1
        elif sorted_arr[mid] > value:
            high = mid - 1
        else:
            first_occurrence = mid
            high = mid - 1  # Look for more occurrences to the left

    if first_occurrence == -1:
        return count

    # Binary search for the last occurrence
    low = 0
    high = len(sorted_arr) - 1
    last_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] < value:
            low = mid + 1
        elif sorted_arr[mid] > value:
            high = mid - 1
        else:
            last_occurrence = mid
            low = mid + 1  # Look for more occurrences to the right

    # Return the count of occurrences
    return last_occurrence - first_occurrence + 1