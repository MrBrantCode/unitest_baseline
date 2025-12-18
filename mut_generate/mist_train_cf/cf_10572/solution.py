"""
QUESTION:
Write a function `find_pairs` that takes a list of integers `lst`, a target number `target`, and a threshold value `threshold` as input, and returns all pairs of numbers in `lst` whose sum equals `target` and whose difference is less than or equal to `threshold`.
"""

def find_pairs(lst, target, threshold):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) <= threshold and lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs