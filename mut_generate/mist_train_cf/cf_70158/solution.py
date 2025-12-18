"""
QUESTION:
Write a function `largestValsFromLabels` that takes four inputs: `values`, `labels`, `num_wanted`, and `use_limit`. The function should return the largest possible sum of a subset `S` of items, where the sum of the indices of items in `S` is minimum. If it is not possible to select `num_wanted` items under the given constraints, return -1. The constraints are:
- The number of items in `S` is at most `num_wanted`.
- For every label `L`, the number of items in `S` with label `L` is at most `use_limit`.
The function should assume that `1 <= values.length == labels.length <= 20000`, `0 <= values[i], labels[i] <= 20000`, `1 <= num_wanted, use_limit <= values.length`.
"""

import heapq
from collections import defaultdict

def largestValsFromLabels(values, labels, num_wanted, use_limit):
    label_counts = defaultdict(int)
    max_heap = []
    total = 0

    for i in range(len(values)):
        heapq.heappush(max_heap, (-values[i], i))

    while max_heap and num_wanted:
        value, index = heapq.heappop(max_heap)
        if label_counts[labels[index]] < use_limit:
            total += -value
            label_counts[labels[index]] += 1
            num_wanted -= 1

    if num_wanted > 0:
        return -1

    return total