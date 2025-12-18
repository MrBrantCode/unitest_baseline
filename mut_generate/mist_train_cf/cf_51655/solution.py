"""
QUESTION:
Create a function called `remove_and_reverse` that takes a list and a value as input. The function should remove all occurrences of the given value from the list and return the modified list in reverse order. It should handle cases where the list is empty or contains only the given value.
"""

def remove_and_reverse(lst, val):
    return [x for x in lst if x != val][::-1]