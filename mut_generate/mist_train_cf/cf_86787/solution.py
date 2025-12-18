"""
QUESTION:
Write a function `shift_list` that takes a list `lst` and an integer `shift` as input and returns a new list with the elements shifted to the left or right by the specified number of positions. The function should handle shift values larger than twice the length of the list, return a new list without modifying the original list, handle empty lists, and have a time complexity of O(n), where n is the length of the list.
"""

def shift_list(lst, shift):
    # Check if the list is empty
    if len(lst) == 0:
        return []

    # Calculate the effective shift value
    shift = shift % len(lst)

    # Shift the elements to the left
    if shift >= 0:
        return lst[shift:] + lst[:shift]
    # Shift the elements to the right
    else:
        return lst[shift:] + lst[:shift]