"""
QUESTION:
Write a function `max_triplet_product(c, target)` that takes in a sorted array `c` of integers and a target integer `target` and returns the maximum product of triplets `(i, j, k)` such that `i < j < k` and `c[i] * c[j] * c[k]` is maximized, where `i`, `j`, and `k` are indices of the array `c`. If no such triplet exists, return 0.
"""

def entance(c, target):
    max_product = 0
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            left, right = j + 1, len(c) - 1
            while left <= right:
                total = c[i] + c[j] + c[right]
                if total == target:
                    max_product = max(max_product, c[i] * c[j] * c[right])
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return max_product