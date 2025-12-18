"""
QUESTION:
Write a function `count_pairs(numbers, target, threshold)` that takes a list of distinct positive integers `numbers`, a target integer `target`, and a threshold integer `threshold` as input, and returns the number of pairs of integers in the list whose sum equals `target` and whose absolute difference is less than or equal to `threshold`, without counting duplicate pairs.
"""

def count_pairs(numbers, target, threshold):
    count = 0
    pairs = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold and numbers[i] + numbers[j] == target:
                pairs.add((min(numbers[i], numbers[j]), max(numbers[i], numbers[j])))
    return len(pairs)