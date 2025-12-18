"""
QUESTION:
Write a function named `most_frequent_over_100` that takes a 2D array of numeric elements as input and returns a dictionary. The dictionary should map each number that occurs most frequently and exceeds 100 to its list of (row, column) indices. If no numbers exceed 100, the function should return an empty list. If multiple numbers exceed 100 with the same highest frequency, the function should include all of them in the output dictionary along with their positions.
"""

def most_frequent_over_100(matrix):
    from collections import Counter

    numbers = [n for row in matrix for n in row if n > 100]
    counter = Counter(numbers)

    if not counter:
        return {}
    
    max_freq = max(counter.values())
    most_frequent_numbers = {n for n, freq in counter.items() if freq == max_freq}

    indices = {}
    for n in most_frequent_numbers:
        indices[n] = [(i, j) for i, row in enumerate(matrix) for j, m in enumerate(row) if m == n]

    return indices