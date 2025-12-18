"""
QUESTION:
Write a function named `count_and_rank_occurrences` that takes an integer sequence (list of integers) as input and returns the occurrence count of each distinct numerical component contained within the sequence. The function should also print the three integers with the highest occurrence count in decreasing order.
"""

from collections import Counter

def count_and_rank_occurrences(lst):
    """
    This function takes an integer sequence as input, returns the occurrence count of each distinct numerical component, 
    and prints the three integers with the highest occurrence count in decreasing order.

    Args:
        lst (list): A list of integers.

    Returns:
        dict: A dictionary with distinct integers as keys and their occurrence counts as values.
    """

    # Create and fill a dictionary with the counts of all unique values.
    count_distinct = Counter(lst)

    # Print the counts.
    for k, v in count_distinct.items():
        print(f"{k}: {v}")

    # Sort these counts in descending order.
    sorted_counts = sorted(count_distinct.items(), key=lambda item: item[1], reverse=True)

    print("\nThe three integers with the highest occurrence count are:")

    # Print first 3 items from sorted counts list
    for i in range(min(3, len(sorted_counts))):
        integer, count = sorted_counts[i]
        print(f"{integer}: {count}")

    return dict(count_distinct)