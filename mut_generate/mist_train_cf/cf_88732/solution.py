"""
QUESTION:
Write a function named `count_occurrences` that takes an array of integers and an integer value as input, and returns the number of occurrences of the given value in the array. The function must have a time complexity of O(n log n) and a space complexity of O(n). The input array will have a maximum length of 10^5 and the input value will be an integer between -10^9 and 10^9.
"""

def count_occurrences(arr, value):
    sorted_arr = sorted(arr)
    count = 0
    
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
            high = mid - 1
    
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
            low = mid + 1
    
    if first_occurrence != -1:
        count = last_occurrence - first_occurrence + 1
    
    return count