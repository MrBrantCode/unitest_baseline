"""
QUESTION:
Write a function `get_filtered_names(names)` that takes a list of names as input and returns a set of names that have a length greater than 6 and do not contain any repeating characters. If no such names exist, return an empty set. Do not use any advanced data structures such as hash maps or sets for intermediate results, only basic data structures like arrays and linked lists are allowed.
"""

def entrance(names):
    result = set()

    for name in names:
        if len(name) > 6:
            is_valid = True
            for i in range(len(name)):
                if name[i] in name[i+1:]:
                    is_valid = False
                    break
            if is_valid:
                result.add(name)

    return result