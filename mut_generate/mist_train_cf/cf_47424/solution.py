"""
QUESTION:
Write a function named `reconstructMatrix` that takes four parameters: `upper`, `middle`, `lower`, and `colsum`. The function should return a list of three lists (`up`, `mid`, and `low`) where each inner list has the same length as `colsum`. The function should distribute the values from `upper`, `middle`, and `lower` to the inner lists based on the values in `colsum`. The distribution rules are as follows: if `colsum[i]` is 3, set `up[i]`, `mid[i]`, and `low[i]` to 1 and decrement `upper`, `middle`, and `lower` by 1. If `colsum[i]` is 2, set one of `up[i]`, `mid[i]`, or `low[i]` to 1 based on the availability of `upper`, `middle`, and `lower`, and decrement the corresponding counter. If `colsum[i]` is 1, set one of `up[i]`, `mid[i]`, or `low[i]` to 1 based on the availability of `upper`, `middle`, and `lower`, and decrement the corresponding counter. If all values from `upper`, `middle`, and `lower` are distributed, return the list of lists; otherwise, return an empty list.
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
        elif colsum[i] == 2:
            if upper > 0:
                up[i] = 1
                upper -= 1
            elif lower > 0:
                low[i] = 1
                lower -= 1
            if middle > 0:
                mid[i] = 1
                middle -= 1
        elif colsum[i] == 1:
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