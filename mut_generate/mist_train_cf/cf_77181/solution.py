"""
QUESTION:
Write a function called `monotonic` that takes a list of elements and a boolean parameter `strict` (defaulting to `False`). The function should return `True` if the sequence of elements in the list is either monotonically increasing or decreasing, considering the `strict` parameter. If `strict` is `True`, consecutive elements are not allowed to be identical; if `strict` is `False`, they may be the same.
"""

def monotonic(l: list, strict: bool = False):
    """
    This function determines if the sequence of elements in the list is either monotonically increasing or decreasing, considering the strictness criterion put in place.
    If the strict parameter is assigned to be True, consecutive elements are not allowed to be identical; however, if it's False, they may be the same.

    """
    # Initialize flags for increasing and decreasing
    increasing = decreasing = True

    # Loop through the list to check sequence
    for i in range(len(l) - 1):
        # If strict is True
        if strict:
            if l[i] <= l[i + 1]:
                increasing = False
            elif l[i] >= l[i + 1]:
                decreasing = False
        # If strict is False
        else:
            if l[i] < l[i + 1]:
                increasing = False
            elif l[i] > l[i + 1]:
                decreasing = False

    # If list is not increasing and not decreasing, return False
    if not increasing and not decreasing:
        return False

    # If the function has not returned yet, it means the list is either increasing or decreasing.
    return True