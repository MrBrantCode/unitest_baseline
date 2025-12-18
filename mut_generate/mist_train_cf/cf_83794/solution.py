"""
QUESTION:
Create a function named `max_value` that takes a multidimensional list of integers as input, containing a mix of positive and negative integers, and returns the maximum value within the list without reordering it. The function should handle empty sublists and lists with a single element correctly, and should not modify the original list arrangement.
"""

def max_value(md_array: list) -> int:
    """Return maximum value of elements in the multidimensional array md_array without reordering it.
    Handles arrays with a mix of positive and negative integers.
    """
    # Base case: If the array is empty, return negative infinity
    if not md_array:
        return float('-inf')

    if isinstance(md_array, list):
        return max(max_value(e) for e in md_array)
    else:
        return md_array