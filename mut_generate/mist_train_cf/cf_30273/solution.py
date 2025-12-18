"""
QUESTION:
Implement a function `sliding_window_count` that takes three inputs: `window_size`, `threshold`, and a list of integers `numbers`. The function should process the list of integers in a sliding window of size `window_size` and count the number of times the sum of the integers in the sliding window is greater than or equal to the given `threshold`. The function should return the count.
"""

def sliding_window_count(window_size, threshold, numbers):
    """
    Counts the number of times the sum of integers in a sliding window 
    of size `window_size` is greater than or equal to the given `threshold`.

    Args:
        window_size (int): Size of the sliding window.
        threshold (int): The threshold value.
        numbers (list): A list of integers.

    Returns:
        int: The count of times the sum of integers in the sliding window 
             is greater than or equal to the threshold.
    """
    count = 0
    window_sum = sum(numbers[:window_size])
    count += 1 if window_sum >= threshold else 0
    
    for i in range(window_size, len(numbers)):
        window_sum = window_sum - numbers[i - window_size] + numbers[i]
        count += 1 if window_sum >= threshold else 0

    return count