"""
QUESTION:
Write a Python function called `merge_duplicates` that takes a list (which may be nested) as input and returns a tuple. The tuple should contain the list with consecutive duplicates merged into a single element and a dictionary with the count of duplicates for each merged element. If the input list is empty, return a message indicating so.
"""

def merge_duplicates(lst):
    if not lst:
        return [], "Empty list provided"
    res = [lst[0]]
    count = {}
    for i in range(1, len(lst)):
        last_element = res[-1]
        if isinstance(last_element, list):
            merged, count_sublist = merge_duplicates(last_element)
            if merged == lst[i]:
                count[tuple(merged)] = count.get(tuple(merged), 1) + 1
                continue
            else:
                res[-1] = merged
        elif last_element == lst[i]:
            count[last_element] = count.get(last_element, 1) + 1
            continue
        res.append(lst[i])
    return res, count