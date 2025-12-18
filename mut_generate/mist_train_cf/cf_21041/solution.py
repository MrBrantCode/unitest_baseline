"""
QUESTION:
Implement a function `count_occurrences` that takes a list of elements as input and returns a dictionary where the keys are the elements from the list and the values are their corresponding counts. The function should not use built-in functions and should have a time complexity of O(n). The function should also be implemented recursively.
"""

def count_occurrences(lst, counts={}):
    if not lst:
        return counts

    item = lst[0]
    counts[item] = counts.get(item, 0) + 1

    return count_occurrences(lst[1:], counts)