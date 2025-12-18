"""
QUESTION:
Write a function `find_triplet(lst, target)` that takes a list of integers `lst` and an integer `target` as input and returns a tuple of three integers from the list that multiply together to give the target product. The function should return the first such triplet it finds, or None if no such triplet exists.
"""

def find_triplet(lst, target):
    n = len(lst)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] * lst[j] * lst[k] == target:
                    return (lst[i], lst[j], lst[k])