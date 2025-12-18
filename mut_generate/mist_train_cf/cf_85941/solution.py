"""
QUESTION:
Construct a function `least_common` that takes a list `lst` and an integer `N` as input, and returns a list of the `N` least common unique elements in `lst`, without duplicates. The function should consider the frequency of each unique element in the list and return the elements with the lowest frequencies.
"""

from collections import Counter

def least_common(lst, N):
    freq_count = Counter(lst)
    return [item for item, count in freq_count.most_common()[:-N-1:-1]]