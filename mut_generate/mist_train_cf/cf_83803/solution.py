"""
QUESTION:
Write a function `advanced_monotonic(l, strict=False)` that determines if the numerical elements in the list `l` are monotonically increasing or decreasing. The function should ignore non-numerical elements in the list and consider the `strict` parameter. If `strict` is `True`, successive elements must not be the same; if `strict` is `False`, repetitive elements are acceptable. The function should return `True` if the list is monotonically increasing or decreasing and `False` otherwise.
"""

def advanced_monotonic(l, strict=False):
    # Initialize the previous_value variable to None
    previous_value = None
    # Initialize monotonically increasing and decreasing indicators
    increasing = True
    decreasing = True

    for item in l:
        try:
            # Firstly, try to convert the item to float for comparison. If this fails, the item is not numerical and
            # should be skipped.
            float_item = float(item)
            if previous_value is not None:
                if float_item > previous_value:
                    decreasing = False
                elif float_item < previous_value:
                    increasing = False
                elif strict:
                    # strict mode is enabled and this element is the same as the last
                    increasing = decreasing = False
            previous_value = float_item
        except (TypeError, ValueError):
            # Skip non-numerical items
            continue
    return increasing or decreasing