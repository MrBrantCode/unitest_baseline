"""
QUESTION:
Write a function `find_pairs(lst, target, threshold)` that finds all pairs of numbers in a list of positive integers `lst` whose sum equals a given `target` number and the absolute difference between the two numbers in the pair is less than or equal to a given `threshold`.
"""

def find_pairs(lst, target, threshold):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) <= threshold and lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs