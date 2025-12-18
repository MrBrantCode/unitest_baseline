"""
QUESTION:
Create a function called `remove_greater_duplicates` that takes a list of integers (`lst`) and an integer value as input. The function should return a new list that contains only the numbers from the original list that are less than or equal to the specified value, with no duplicates. The order of the numbers in the original list does not need to be preserved in the output.
"""

def remove_greater_duplicates(lst, value):
    # Remove numbers greater than the specified value and remove duplicates
    return list(set([x for x in lst if x <= value]))