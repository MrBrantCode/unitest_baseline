"""
QUESTION:
Write a function `reduce_list(lst)` that takes a list containing integers and/or strings as input and returns a list of at most 5 distinct elements. The function should dismiss the least frequent elements first, prioritizing elements by their appearance order in the list if their frequencies are equal.
"""

from collections import Counter

def reduce_list(lst):
    counter = Counter(lst)
    order = {v: i for i, v in enumerate(lst)}
    while len(counter) > 5:
        least_frequent = sorted(counter.items(), key=lambda x: (x[1], order[x[0]]))[0][0]
        del counter[least_frequent]
    return list(counter.keys())