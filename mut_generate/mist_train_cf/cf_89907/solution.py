"""
QUESTION:
Write a function named `generate_binary_strings` that takes an integer `N` as input, generates all possible binary strings of length `N` with an equal number of 0s and 1s, and returns them as a list. The function should be optimized to minimize time complexity and handle large values of `N` efficiently.
"""

def generate_binary_strings(N):
    result = []
    def backtrack(current, count_0, count_1):
        if count_0 > N // 2 or count_1 > N // 2:
            return
        if len(current) == N:
            result.append(current)
            return
        backtrack(current + '0', count_0 + 1, count_1)
        backtrack(current + '1', count_0, count_1 + 1)
    backtrack('', 0, 0)
    return result