"""
QUESTION:
Write a function named `example_func` that takes a list as an input and returns a new list where all integers (including those in nested lists) have '5' added to them. The function should handle nested lists of arbitrary depth and not modify the original list. It should also handle non-integer elements (including strings and floats) without modification.
"""

def example_func(lst):
    def process_item(item):
        if isinstance(item, list):
            return example_func(item)
        elif isinstance(item, int):
            return item + 5
        return item

    return [process_item(item) for item in lst]