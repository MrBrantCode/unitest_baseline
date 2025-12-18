"""
QUESTION:
Write a function named `find_recurring_elements` that takes a list of integers as input and returns a list of integers that appear more than once in the input list.
"""

def find_recurring_elements(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    recurring_elements = []
    for key, value in count_dict.items():
        if value > 1:
            recurring_elements.append(key)

    return recurring_elements