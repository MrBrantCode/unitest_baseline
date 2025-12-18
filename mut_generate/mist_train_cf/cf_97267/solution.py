"""
QUESTION:
Create a function `iterate_until_threshold` that takes a list of integers as input and iterates over its elements. The function should keep track of the sum of elements encountered so far and break the iteration when this sum exceeds the product of the previous two elements. The function should also keep track of the maximum element encountered. The function should return a tuple containing the sum and the maximum element when the iteration breaks. The time complexity of the function should be O(n), where n is the length of the list.
"""

def iterate_until_threshold(lst):
    """
    Iterate over a list of integers until the sum of elements exceeds the product of the previous two elements.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum and the maximum element when the iteration breaks.
    """
    sum_so_far = 0
    max_element = float('-inf')

    for i, num in enumerate(lst):
        sum_so_far += num
        if i > 1 and sum_so_far > lst[i-1] * lst[i-2]:
            break
        max_element = max(max_element, num)

    return sum_so_far, max_element