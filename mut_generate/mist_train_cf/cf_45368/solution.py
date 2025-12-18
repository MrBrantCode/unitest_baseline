"""
QUESTION:
Write a function `descriptive_stats` that takes a list of numbers as input, calculates and returns the median, mode, range, and interquartile range without using built-in functions. The function should handle lists containing negative numbers, positive numbers, zeros, and duplicates. If there are multiple modes, return `None` for the mode.
"""

def descriptive_stats(l: list):
    l = sorted(l)
    length = len(l)
    
    # median
    if length % 2 != 0:
        median = l[length // 2]
    else:
        median = (l[length // 2] + l[length // 2 - 1]) / 2

    # mode
    num_counts = {}
    for num in l:
        num_counts[num] = num_counts.get(num, 0) + 1
    max_count = max(num_counts.values())
    mode = [k for k, v in num_counts.items() if v == max_count]
    mode = mode[0] if len(mode) == 1 else None

    # range
    range_ = l[-1] - l[0]

    # interquartile range
    if len(l) % 2 == 0:
        q1 = (l[length // 4] + l[length // 4 - 1]) / 2
        q3 = (l[-(length // 4)] + l[-(length // 4 + 1)]) / 2
    else:
        q1 = l[length // 4]
        q3 = l[-(length // 4 + 1)]
    iqr = q3 - q1

    return {'Median': median, 'Mode': mode, 'Range': range_, 'Interquartile Range': iqr}