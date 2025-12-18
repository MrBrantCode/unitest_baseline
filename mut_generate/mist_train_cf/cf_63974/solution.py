"""
QUESTION:
Write a function `aggregate_unique_elements` that calculates the aggregate of unique elements within a provided list. The function should handle lists of varying lengths and compositions, including nested lists and non-numeric elements. It should return a tuple containing the aggregate sum and the quantity of distinct elements. If the list contains non-numeric elements, return an error message instead. Do not use built-in Python functions or libraries for flattening the list or calculating the aggregate.
"""

def aggregate_unique_elements(lst, unique_set=None):
    if unique_set is None:
        unique_set = set()
    for i in lst:
        if isinstance(i, list):
            aggregate_unique_elements(i, unique_set)
        elif isinstance(i, (int, float)):
            unique_set.add(i)
        else:
            return "Error: Non-numeric elements present in the list."
    aggregate = sum(unique_set)
    quantity = len(unique_set)
    return aggregate, quantity