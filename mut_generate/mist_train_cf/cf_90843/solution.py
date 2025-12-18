"""
QUESTION:
Implement a function named `find_most_common` that takes a list of elements as input and returns the most frequently occurring element in the list. You cannot use any built-in functions or methods that directly solve the problem, such as the `collections` module or the `Counter` class. The function should handle any type of elements that can be compared for equality. If there are multiple elements with the same highest frequency, the function can return any one of them.
"""

def find_most_common(lst):
    counts = {}

    for elem in lst:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    most_common = None
    max_count = 0

    for elem, count in counts.items():
        if count > max_count:
            most_common = elem
            max_count = count

    return most_common