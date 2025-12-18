"""
QUESTION:
Write a function `median` that takes a list of numbers as input and returns the median without sorting the list in any order. The function should handle lists with both even and odd numbers of elements. If the list is empty, return `None`.
"""

def find_median(l: list):
    if not l:
        return None

    length = len(l)
    s_l = sorted(l)

    if length % 2 == 0:
        mid_1 = s_l[int(length / 2) - 1]
        mid_2 = s_l[int(length / 2)]
        return (mid_1 + mid_2) / 2
    else:
        return s_l[int(length / 2)]