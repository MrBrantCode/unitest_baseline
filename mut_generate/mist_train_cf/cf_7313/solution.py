"""
QUESTION:
Write a function `find_median` that calculates the median of an array of numbers. The function should handle arrays with both odd and even numbers of elements, returning the middle value for odd arrays and the average of the two middle values for even arrays. It should also handle arrays with duplicate elements by ignoring them when calculating the median. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the input array.
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