"""
QUESTION:
Write a function `most_frequent_value(lst)` that takes a list `lst` as input, which can contain up to 1 million elements of any type, including strings and integers. The function should return the most frequent value in the list. If the most frequent value is a string, return it as a string; otherwise, return it as an integer.
"""

from collections import Counter

def most_frequent_value(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0][0]
    return str(most_common) if isinstance(most_common, str) else int(most_common)