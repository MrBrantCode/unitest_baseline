"""
QUESTION:
Create a function `sum_with_exclusion(n, exclude_lst)` that takes an integer `n` and a list of integers `exclude_lst` as arguments. The function should return the sum of all numbers from 1 to `n` excluding the integers present in `exclude_lst`. The function should handle cases where `n` is less than 1 and where integers in `exclude_lst` are not within the 1 to `n` range.
"""

def sum_with_exclusion(n, exclude_lst):
    if n < 1:
        return 0   
    return sum(i for i in range(1, n + 1) if i not in exclude_lst)