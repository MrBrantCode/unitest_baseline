"""
QUESTION:
Write a function `reconstructMatrix` that takes four parameters: `upper`, `middle`, `lower`, and `colsum`. The function should return a 3D integer array representing a 3-row binary matrix with `n` columns, where `n` is the length of `colsum`. The sum of elements in the 0-th row is `upper`, the sum of elements in the 1-st row is `middle`, and the sum of elements in the 2-nd row is `lower`. The sum of elements in the i-th column is `colsum[i]`. If there are multiple valid solutions, return the one where the sum of the binary values in the upper row is maximized. If there are still multiple solutions, maximize the sum in the middle row. If no valid solution exists, return an empty 3D array.
"""

def reconstructMatrix(upper, middle, lower, colsum):
    n = len(colsum)
    up = [0]*n
    mid = [0]*n
    low = [0]*n
    for i in range(n):
        if colsum[i] == 3:
            up[i] = mid[i] = low[i] = 1
            upper -= 1
            middle -= 1
            lower -= 1
        if colsum[i] == 2:
            if upper > 0:
                up[i] = 1
                upper -= 1
            elif lower > 0:
                low[i] = 1
                lower -= 1
            if middle > 0:
                mid[i] = 1
                middle -= 1
        if colsum[i] == 1:
            if upper > 0:
                up[i] = 1
                upper -= 1
            elif middle > 0:
                mid[i] = 1
                middle -= 1
            elif lower > 0:
                low[i] = 1
                lower -= 1
    if upper == 0 and middle == 0 and lower == 0:
        return [up, mid, low]
    else:
        return []