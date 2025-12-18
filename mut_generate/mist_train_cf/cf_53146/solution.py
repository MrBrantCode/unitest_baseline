"""
QUESTION:
Implement a function named `compute_mean_median_mode` that takes a list of integers as input and returns a tuple containing the mean, median, and mode values of the list. The function should handle edge cases where the list has a length of 0 or 1, returning None for all values in the former case and the single element for all values in the latter case. The function should not use Python's built-in functions for calculating mean, median, and mode.
"""

def compute_mean_median_mode(arr):
    if not arr:
        return None, None, None
    elif len(arr) == 1:
        return arr[0], arr[0], arr[0]
    else:
        sorted_arr = sorted(arr)
        mean = sum(sorted_arr) / len(sorted_arr)
        
        if len(sorted_arr) % 2 == 0:
            median = (sorted_arr[len(sorted_arr) // 2 - 1] + sorted_arr[len(sorted_arr) // 2]) / 2
        else:
            median = sorted_arr[len(sorted_arr) // 2]
            
        num_counts = {}
        for num in sorted_arr:
            num_counts[num] = num_counts.get(num, 0) + 1
        max_count = max(num_counts.values())
        mode = [num for num, count in num_counts.items() if count == max_count]
        
        return mean, median, mode