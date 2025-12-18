"""
QUESTION:
Develop a function `find_occurrences(lst, target)` to find the first and last occurrence of a target value in a sorted list `lst` and the number of occurrences of each unique value in the list. The function should handle cases where the target value does not exist in the list or the list is empty, returning an error message in these cases.
"""

def find_occurrences(lst, target):
    if len(lst) == 0:
        return "The list is empty."

    if target not in lst:
        return f"The target value '{target}' does not exist in the list."

    first = lst.index(target)
    last = len(lst) - 1 - lst[::-1].index(target)
    counts = {}
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return {"First Occurrence": first, "Last Occurrence": last, "Counts": counts}