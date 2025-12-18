"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of numbers as input and returns a new list containing the remaining elements in their original order after removing all duplicated entries. The function should have a time complexity of O(n).
"""

def remove_duplicates(num_list):
    seen = set()
    return [x for x in num_list if not (x in seen or seen.add(x))]