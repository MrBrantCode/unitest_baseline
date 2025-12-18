"""
QUESTION:
Write a function `filter_merge_sort_even_numbers` that takes two lists of integers `l1` and `l2` as input, extracts all even numbers from both lists, combines them into a single list, and returns the combined list in descending numerical order. The function should use a helper function to merge and sort the list.
"""

def filter_merge_sort_even_numbers(l1: list, l2: list) -> list:
    """
    Extracts exclusively even numbers from a pair of lists, combines, sorts them in descending numerical order.
    """

    def helper(m: list) -> list:
        """Helper function to sort and return the list in descending order."""
        m.sort(reverse=True)
        return m

    collection_even = [element for element in l1+l2 if element % 2 == 0]
    return helper(collection_even)