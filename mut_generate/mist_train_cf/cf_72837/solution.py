"""
QUESTION:
Create a recursive function called `smallest_unique` that takes a list of integers as input and returns the smallest unique integer value present in the list. The input list can contain up to 10^5 elements, and the integers range from -10^5 to 10^5.
"""

def smallest_unique(input_list, current=None):
    if len(input_list) == 0:
        return current
    head, *tail = input_list
    if current is None or (head < current and input_list.count(head)==1):
        current = head
    return smallest_unique(tail, current)