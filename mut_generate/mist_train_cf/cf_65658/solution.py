"""
QUESTION:
Create a function called `filter_items` that takes a list of items and two functions as arguments. The function should filter the items based on a predicate function `pred_fn` and apply a transformation function `transform_fn` to the filtered items.

The `pred_fn` should implement multiple logical stages, and the `transform_fn` should alter the `value` attribute of each item. The `filter_items` function should have a time complexity of O(n) and should not exceed the list length of 10,000 items or item values of 1000.

Constraints:
* 1 <= list length <= 10000
* 0 <= item.value <= 1000
"""

def filter_items(lst, pred_fn, transform_fn):
    """
    Filters a list of items based on a predicate function and applies a transformation function.

    Args:
    lst (list): A list of items.
    pred_fn (function): A function that takes an item and returns a boolean.
    transform_fn (function): A function that takes an item and returns a transformed item.

    Returns:
    list: A list of transformed items that satisfy the predicate function.
    """
    return [transform_fn(item) for item in lst if pred_fn(item)]