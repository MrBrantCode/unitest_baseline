"""
QUESTION:
Create a function `odd_numbers` that takes a nested list of integers as input and returns a new list containing only the odd numbers. The function should work for lists of varying depths of nesting, using list comprehension to construct the output list. Assume that all elements in the input list are either integers or lists, with no other types present.
"""

def odd_numbers(nested_list):
    def flatten(nested):
        for item in nested:
            if isinstance(item, int):
                yield item
            else:
                yield from flatten(item)

    return [i for i in flatten(nested_list) if i % 2 != 0]