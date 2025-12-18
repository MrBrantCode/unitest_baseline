"""
QUESTION:
Write a function `max_common_chars(s1, s2, n)` that takes two strings `s1` and `s2` and an integer `n` as input, and returns the maximum number of non-repeated common characters between the two strings after distributing `n` deletions among them. The deletions should be distributed in a way that maximizes the number of non-repeated common characters.
"""

from collections import Counter

def max_common_chars(s1, s2, n):
    # count characters in each string
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    # distribute deletions
    for char, count in counter1.items():
        if count > counter2[char]:
            deletions = min(count - counter2[char], n)
            counter1[char] -= deletions
            n -= deletions
        if n == 0:
            break

    for char, count in counter2.items():
        if count > counter1[char]:
            deletions = min(count - counter1[char], n)
            counter2[char] -= deletions
            n -= deletions
        if n == 0:
            break

    # calculate max non-repeated common characters
    return sum(min(counter1[char], counter2[char]) for char in counter1.keys())