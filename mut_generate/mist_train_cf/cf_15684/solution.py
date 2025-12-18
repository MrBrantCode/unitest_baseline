"""
QUESTION:
Write a function `count_occurrences(item, lst)` that counts the occurrences of `item` in a given list `lst`. The function should also count occurrences of `item` in nested lists and dictionaries that directly contain `item`, but ignore any nested lists or dictionaries that are contained within another nested list or dictionary. The function should return the total count of occurrences of `item` in `lst`.
"""

def count_occurrences(item, lst):
    count = 0

    def helper(obj):
        nonlocal count

        if isinstance(obj, list):
            for elem in obj:
                helper(elem)
        elif isinstance(obj, dict):
            for val in obj.values():
                helper(val)
        else:
            if obj == item:
                count += 1

    helper(lst)
    return count