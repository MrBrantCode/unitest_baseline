"""
QUESTION:
Create a function called `remove_duplicates` that uses a list comprehension to create a copy of a given list while excluding any duplicate elements. The input will be a list of elements and the output should be a new list containing the unique elements from the original list.
"""

def remove_duplicates(input_list):
    """Return a new list containing the unique elements from the input list."""
    new_list = []
    [new_list.append(x) for x in input_list if x not in new_list]
    return new_list