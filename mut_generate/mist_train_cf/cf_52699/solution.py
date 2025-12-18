"""
QUESTION:
Write a function named `longest_distinct_subsequence` that takes a sequence of integers as input and returns a tuple containing the maximum number of distinct numbers and the longest continuous subsequence containing them. The subsequence should be as long as possible. Use a sliding window approach and consider edge cases where the input sequence may be empty, contain all the same numbers, or contain all distinct numbers.
"""

def longest_distinct_subsequence(sequence):
    """
    This function takes a sequence of integers as input and returns a tuple containing 
    the maximum number of distinct numbers and the longest continuous subsequence containing them.

    Args:
        sequence (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum number of distinct numbers and the longest 
        continuous subsequence containing them.
    """

    # Handle edge case where the sequence is empty
    if not sequence:
        return 0, []

    # Initialize variables to keep track of the maximum number of distinct numbers and 
    # the longest subsequence containing them
    max_distinct = 0
    longest_subsequence = []

    # Initialize variables for the sliding window
    window_start = 0
    distinct_count = 0
    num_count = {}

    # Traverse through the sequence
    for window_end in range(len(sequence)):
        # Add the current number to the window
        right_num = sequence[window_end]
        if right_num not in num_count:
            num_count[right_num] = 0
            distinct_count += 1
        num_count[right_num] += 1

        # Shrink the window from the left if the current number is a duplicate
        while num_count[right_num] > 1:
            left_num = sequence[window_start]
            num_count[left_num] -= 1
            if num_count[left_num] == 0:
                distinct_count -= 1
                del num_count[left_num]
            window_start += 1

        # Update the maximum number of distinct numbers and the longest subsequence
        if distinct_count > max_distinct:
            max_distinct = distinct_count
            longest_subsequence = sequence[window_start:window_end + 1]

    return max_distinct, longest_subsequence