"""
QUESTION:
Construct a function `find_max_min_avg(arr)` that takes an array of integers as input, removes any duplicate elements, and finds the maximum, minimum, and average values of the array. The array contains positive integers ranging from 1 to 1000 and has a length between 10 and 1000 elements. Ensure the function runs in O(n) time complexity, where n is the length of the array.
"""

def find_max_min_avg(arr):
    # Remove duplicates from the array
    arr = list(set(arr))

    # Initialize variables for maximum, minimum, and sum
    max_val = arr[0]
    min_val = arr[0]
    sum_val = 0

    # Iterate through the array
    for num in arr:
        # Find maximum element
        if num > max_val:
            max_val = num
        
        # Find minimum element
        if num < min_val:
            min_val = num
        
        # Calculate sum of elements
        sum_val += num
    
    # Calculate average
    avg_val = sum_val / len(arr)

    # Return the maximum, minimum, and average values
    return {
        "max": max_val,
        "min": min_val,
        "avg": avg_val
    }