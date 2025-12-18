"""
QUESTION:
Write a function named `get_sublist` that takes a list of integers `lst`, an integer `threshold`, and an integer `divisor` as parameters. The function should return a new list containing elements from `lst` that are greater than `threshold` and divisible by `divisor`, sorted in descending order. The function must not use built-in functions like `filter()`, `sorted()`, or list comprehensions.
"""

def get_sublist(lst, threshold, divisor):
    sublist = []

    for element in lst:
        if element > threshold and element % divisor == 0:
            sublist.append(element)

    for i in range(len(sublist)):
        for j in range(i + 1, len(sublist)):
            if sublist[i] < sublist[j]:
                sublist[i], sublist[j] = sublist[j], sublist[i]

    return sublist