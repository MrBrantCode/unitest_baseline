"""
QUESTION:
Write a function `longest_unique_subsequence` that takes a list of integers as input and returns the length of the longest unbroken subsequence with unique integers. The function should handle sequences with and without repetitions, and it should return the length of the entire sequence if there are no repetitions, or 1 if the sequence consists of identical elements.
"""

def longest_unique_subsequence(sequence):
    """
    This function takes a list of integers as input and returns the length of the longest unbroken subsequence with unique integers.

    Args:
        sequence (list): A list of integers.

    Returns:
        int: The length of the longest unbroken subsequence with unique integers.
    """

    # Initialize variables to keep track of the maximum length and the current window
    max_length = 0
    left = 0
    char_set = set()

    # Iterate over the sequence
    for right in range(len(sequence)):
        # While the current element is in the set, remove the leftmost element from the set and move the left pointer to the right
        while sequence[right] in char_set:
            char_set.remove(sequence[left])
            left += 1

        # Add the current element to the set
        char_set.add(sequence[right])

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length