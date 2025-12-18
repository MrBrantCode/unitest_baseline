"""
QUESTION:
Write a function `filter_max_float` that takes a list of strings as input, where each string represents a comma-separated sequence of numeric values, and returns a new list containing only the sequences that do not contain the maximum representable floating-point number (1.7e+308).
"""

from typing import List

def filter_max_float(datas: List[str]) -> List[List[float]]:
    cols = []
    for data in datas:
        col = [float(_it) for _it in data.split(',') if _it.strip() != '']
        if 1.7e+308 not in col:
            cols.append(col)
    return cols