"""
QUESTION:
Create a function named `mean_and_median` that takes an array of positive integers as input, calculates the mean and median of the numbers, and returns a string representation of the results. The function should handle duplicate numbers and non-integer inputs by providing an error message. The input array should contain only integers between 1 and 1000, inclusive. If the input is invalid (not a list, contains non-positive integers, contains non-integer values, etc.), the function should return an error message.
"""

def mean_and_median(arr):
    # Check if the input is valid
    if not isinstance(arr, list):
        return "Invalid input: Input must be a list of positive integers."
    if not all(isinstance(x, int) and x > 0 and x <= 1000 for x in arr):
        return "Invalid input: Input must contain only positive integers between 1 and 1000."
    
    # Calculate the mean and median
    n = len(arr)
    mean = sum(arr) / n
    sorted_arr = sorted(arr)
    median = sorted_arr[n // 2] if n % 2 == 1 else (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    
    # Return the result as a string
    return f"Mean: {mean}, Median: {median}"