"""
QUESTION:
Write a function `mean_and_median(arr)` that takes a list of positive integers (1 ≤ n ≤ 1000) and returns a string representing the mean and median of the numbers. The function should handle non-integer inputs by returning an error message "Invalid input: Input must contain only positive integers." and non-list inputs by returning an error message "Invalid input: Input must be a list of positive integers.".
"""

def mean_and_median(arr):
    # Check if the input is valid
    if not isinstance(arr, list):
        return "Invalid input: Input must be a list of positive integers."
    if not all(isinstance(x, int) and x > 0 for x in arr):
        return "Invalid input: Input must contain only positive integers."
    
    # Calculate the mean and median
    n = len(arr)
    mean = sum(arr) / n
    sorted_arr = sorted(arr)
    median = sorted_arr[n // 2] if n % 2 == 1 else (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    
    # Return the result as a string
    return f"Mean: {mean}, Median: {median}"