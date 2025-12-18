"""
QUESTION:
Write a function named `minCost` that takes two arrays `heights` and `weights` as input, where `1 <= heights.length, weights.length <= 100` and `1 <= heights[i], weights[i] <= 100`. The function should return the minimum total cost of moving students to their correct positions in a line, where the cost of moving a student is equal to their weight and the correct positions are in non-decreasing order of height. The function should have a time complexity of `O(n log n)` due to sorting.
"""

def minCost(heights, weights):
    expected = sorted(heights)
    total_cost = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            total_cost += weights[i]
    return total_cost