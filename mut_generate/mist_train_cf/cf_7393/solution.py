"""
QUESTION:
Write a function `generate_binary_strings(N)` to generate all possible binary strings of length N that have an equal number of 0s and 1s. The function should be optimized to handle large values of N efficiently. The function should return a list of all generated binary strings.
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