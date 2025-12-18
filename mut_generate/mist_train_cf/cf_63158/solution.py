"""
QUESTION:
Implement the function `get_positive_and_sort(l: list)` to return only the positive numbers in the list, sorted in ascending order, without using any external libraries or built-in sorting functions besides the `sorted` function in Python. The function should not return any duplicate values and should handle empty or null input lists. The function should be able to handle lists with a mix of positive, negative integers, and zeros.
"""

def get_positive_and_sort(l: list):
    """Return only positive numbers in the list, sorted in ascending order.
    """
    # Step 1: Filter positive numbers
    positive_nums = [num for num in l if num > 0 and isinstance(num, (int))]
    
    # Step 2: Sort the positive numbers
    return sorted(set(positive_nums))