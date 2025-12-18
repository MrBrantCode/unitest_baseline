"""
QUESTION:
Create a function `find_median` that takes a list of integers `arr` as input. The function should calculate the median of the array, excluding duplicates. It should have a maximum time complexity of O(n) for the median calculation and a maximum space complexity of O(1). The function should handle arrays with an odd number of unique elements by returning the middle value, and arrays with an even number of unique elements by returning the average of the two middle values.
"""

def find_median(arr):
    # Remove duplicates from the array
    unique_arr = list(set(arr))
    n = len(unique_arr)

    # Sort the array in ascending order
    for i in range(n):
        for j in range(0, n-i-1):
            if unique_arr[j] > unique_arr[j+1]:
                unique_arr[j], unique_arr[j+1] = unique_arr[j+1], unique_arr[j]

    # Calculate the median
    if n % 2 == 0:
        # If the array has an even number of elements
        median = (unique_arr[n//2] + unique_arr[n//2 - 1]) / 2
    else:
        # If the array has an odd number of elements
        median = unique_arr[n//2]

    return median