"""
QUESTION:
Create a function `sort_third(l: list)` that takes a list `l` and returns a new list where all elements at positions that are multiples of 3 are replaced with the corresponding elements from `l` in descending order, while other elements remain unchanged. The list is 1-indexed, meaning the first element is considered to be at position 1, not 0.
"""

def sort_third(l: list):
    multiples_of_three = sorted([l[i] for i in range(len(l)) if (i + 1) % 3 == 0], reverse=True)
    for i, value in enumerate(l):
        if (i + 1) % 3 == 0:
            l[i] = multiples_of_three.pop(0)
    return l