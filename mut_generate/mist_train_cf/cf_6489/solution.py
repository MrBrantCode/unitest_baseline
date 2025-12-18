"""
QUESTION:
Create a function `count_combinations` that takes two parameters: an integer `N` and a list of integers `A`. The function should return the maximum number of unique combinations of numbers from `A` that add up to `N`, with a time complexity of O(2^N) and a space complexity of O(N).
"""

def count_combinations(N, A):
    combinations = [0] * (N + 1)
    combinations[0] = 1

    for num in A:
        for i in range(num, N + 1):
            combinations[i] += combinations[i - num]

    return combinations[N]