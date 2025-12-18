"""
QUESTION:
Write a Python function named `count_number_frequency` that takes a multi-dimensional list of integers and a target number as input, counts the frequency of the target number in each sublist and the overall frequency in all sublists, and returns the results. The function should handle cases where the target number does not appear in a specific sublist.
"""

def count_number_frequency(numbers, target):
    """
    Counts the frequency of a target number in each sublist and the overall frequency in all sublists.

    Args:
        numbers (list): A multi-dimensional list of integers.
        target (int): The target number to count.

    Returns:
        A list of frequencies for each sublist and the overall frequency.
    """
    # Initialize a variable to keep track of the overall count
    overall_count = 0
    # Initialize a list to store the count for each sublist
    sublist_counts = []

    # Iterate through the sublists
    for i, sublist in enumerate(numbers):
        # Count the occurrences of the target number in the sublist
        sublist_count = sublist.count(target)
        # Add the count to the overall count
        overall_count += sublist_count
        # Append the count to the sublist counts list
        sublist_counts.append(sublist_count)

    # Return the sublist counts and the overall count
    return sublist_counts, overall_count