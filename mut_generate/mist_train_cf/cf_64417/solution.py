"""
QUESTION:
Create a function named `alternate_base_weighted_avg` that takes four parameters: two positive integers `n` and `m` where `n` is less than or equal to `m`, an integer `base` denoting a number system within the boundary [2,10] (inclusive), and an alternate function `alternate_fn` that returns two weights for `n` and `m`. The function should compute a weighted average for the series of numbers from `n` to `m` (both inclusive) using the `alternate_fn`, round off the average to the closest integer, and convert it to a numeral in the specified number system. Return -1 if either `n` surpasses `m` or `base` exceeds the permissible range.
"""

def alternate_base_weighted_avg(n, m, base, alternate_fn):
    if n > m:
        return -1
    if base < 2 or base > 10:
        return -1
    
    total, total_weight = 0, 0
    for i in range(n, m + 1):
        weight_i, weight_end = alternate_fn(i, m)
        total += i * weight_i
        total_weight += weight_i
        
    if total_weight == 0:
        return format(0, '#'+str(base+1)+'b')
        
    res = int(round(total / total_weight))
    if base == 10:
        return str(res)
    elif base == 2:
        return format(res, '#0b')   
    elif base == 8:
        return format(res, '#0o')   
    else:
        return format(res, '#'+str(base+1)+'x')