"""
QUESTION:
Write a function `find_max_subset(arr, K)` that returns a subset of size K from the given array `arr` with the maximum possible sum. The function should return the subset of the original array, not the sorted array. The array can contain duplicate elements, and the subset must contain distinct elements from the original array.
"""

def find_max_subset(arr, K):
    arr.sort(reverse=True)  # Sort the array in descending order
    max_sum = 0
    window_sum = sum(arr[:K])  # Calculate the sum of the first window
    max_sum = max(max_sum, window_sum)  # Update max_sum if necessary

    for i in range(K, len(arr)):
        window_sum += arr[i] - arr[i - K]  # Slide the window one position to the right
        max_sum = max(max_sum, window_sum)  # Update max_sum if necessary

    return arr[:K]  # Return the subset corresponding to the window with the maximum sum