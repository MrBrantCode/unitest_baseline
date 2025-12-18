"""
QUESTION:
Write a function `shift_list(lst, shift)` that takes a list `lst` and an integer `shift` as input, and returns a new list where the elements of `lst` have been shifted `shift` positions to the left. If `shift` is negative, the elements are shifted to the right instead. The function should handle cases where `shift` is larger than the length of `lst`, and should also handle empty lists by returning an empty list without modifying the original list.
"""

def shift_list(lst, shift):
    # Check for empty list
    if not lst:
        return []

    # Calculate the effective shift value
    shift %= len(lst)

    # Shift the elements to the left or right depending on the sign of shift
    if shift >= 0:
        return lst[shift:] + lst[:shift]
    else:
        return lst[shift:] + lst[:shift+len(lst)]