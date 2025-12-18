"""
QUESTION:
Create a function `add_lists(list1, list2)` that takes two lists of numbers as input, ensures they have the same length and are both longer than 2, and returns a new list where corresponding values are added together, unless both values are divisible by 3, in which case their product is used instead.
"""

def add_lists(list1, list2):
    if len(list1) != len(list2) or len(list1) < 3 or len(list2) < 3:
        return "Error: The length of both lists should be equal and greater than 2."

    return [x * y if x % 3 == 0 and y % 3 == 0 else x + y for x, y in zip(list1, list2)]