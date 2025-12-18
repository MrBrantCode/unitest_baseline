"""
QUESTION:
Implement a function `get_positive_multiply_and_sort(l, n)` that takes a list of integers `l` and an integer `n` as input, returns a list of positive numbers from `l` multiplied by `n` and sorted in ascending order. The function should utilize two helper functions: `multiply_elements` to multiply the positive numbers by `n`, and `sort_elements` to sort elements in ascending order.
"""

def get_positive_multiply_and_sort(l: list, n: int):
    """Return only positive numbers in the list multiplied by n and sorted in ascending order."""
    def multiply_elements(lst: list, multiplier: int):
        """Helper function to multiply the positive numbers"""
        return [i * multiplier for i in lst]

    def sort_elements(lst: list):
        """Helper function for sorting elements"""
        return sorted(lst)

    # Filter out non positive numbers
    l = [num for num in l if num > 0]
    # Multiply all positive numbers by n
    l = multiply_elements(l, n)
    # Sort the list in ascending order
    return sort_elements(l)