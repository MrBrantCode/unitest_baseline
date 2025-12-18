"""
QUESTION:
Write a function named `eliminate_successive_duplicates` that takes a list as input and returns a new list with all successive identical elements removed.
"""

def eliminate_successive_duplicates(lst):
    new_list = [v for i, v in enumerate(lst) if i == 0 or v != lst[i-1]]
    return new_list