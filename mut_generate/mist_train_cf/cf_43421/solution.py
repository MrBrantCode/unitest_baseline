"""
QUESTION:
Create a function named `combine_and_sort_lists` that takes two lists of dictionaries as input, where each dictionary contains 'name', 'grade', and 'age' properties. The function should combine the two lists, remove any duplicates (based on 'name', 'grade', and 'age'), and sort the resulting list first by 'grade' in ascending order, then by 'age' in descending order, and finally by 'name' in ascending order.
"""

def combine_and_sort_lists(list1, list2):
    # Combine the two lists
    combined = list1 + list2
    # Use a set to remove any duplicates by converting each dictionary to a frozenset
    unique_combined = [dict(s) for s in set(frozenset(d.items()) for d in combined)]
    # Sort the combined list by the required criteria
    sorted_unique_combined = sorted(unique_combined, key=lambda x: (x['grade'], -x['age'], x['name']))
    return sorted_unique_combined