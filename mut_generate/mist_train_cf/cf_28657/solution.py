"""
QUESTION:
Generate the `generate_final_table(table_list, row)` function that takes in a 2D list of integers `table_list` and an integer `row`, and returns a new 2D list of integers. If the number of rows in `table_list` is more than 1, the function should create a new 2D list with the same number of rows as `table_list` plus 2, and the same number of columns as the first sublist of `table_list` plus 2. The value at the specified row and column 2 should be "x", and all other values should be 0. If the number of rows in `table_list` is not more than 1, the function should return `table_list`.
"""

from typing import List

def entance(table_list: List[List[int]], row: int) -> List[List[int]]:
    if len(table_list) > 1:
        final_table = [[0 for _ in range(len(table_list[0]) + 2)] for _ in range(len(table_list) + 2)]
        final_table[row][2] = 'x'
        return final_table
    else:
        return table_list