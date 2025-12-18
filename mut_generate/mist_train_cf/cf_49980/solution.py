"""
QUESTION:
Write a function named `find_perfect_squares` that takes two integers `start` and `end` as input and returns the count of perfect squares between `start` and `end` (inclusive) along with the perfect squares themselves in descending order. The function should handle negative input by returning an error message and should also handle cases where `start` is greater than `end`. The function should be efficient enough to handle large numbers, with a time complexity of approximately O(sqrt(n)).
"""

def find_perfect_squares(start, end):
    if start < 0 or end < 0:
        return "Error: Input should not be negative"
    elif start > end:
        return "Error: End value should be greater than start value"
    else:
        perfect_squares = [i*i for i in range(int(end**0.5), int(start**0.5) - 1, -1) if i*i >= start]
        return len(perfect_squares), perfect_squares