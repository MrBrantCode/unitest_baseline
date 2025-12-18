"""
QUESTION:
Develop a function named `weighted_avg_custom_base` that takes four parameters: two positive whole numbers `n` and `m` where `n` is less than or equal to `m`, a discount factor `d` within the range of 1 to `m-n+1`, and a base number system `base` between 2 and 20. 

The function should calculate the weighted average of whole numbers from `n` to `m` (inclusive), where the weights are determined by the quantity of divisors of each number discounted by `d`. The resulting average should be rounded to the closest whole number and converted to the custom base system. 

Return the custom base representation of the weighted average as a string. If `n` exceeds `m`, `d` is outside the permitted range, or `base` is outside the assigned limit, return -1.
"""

def weighted_avg_custom_base(n, m, base, d):
    if not(n <= m and 1 <= d <= m-n+1 and 2 <= base <= 20):
        return -1
    
    num_and_weights = []
    for i in range(n, m+1):
        factors = sum([1 for j in range(1, i+1) if i % j == 0])
        num_and_weights.append((i, factors-d))

    weighted_sum, total_weight = 0, 0
    for num, weight in num_and_weights:
        weighted_sum += num * weight
        total_weight += weight

    if total_weight == 0:
        return -1
    avg = round(weighted_sum / total_weight)

    if base == 10:
        return str(avg)
    elif base == 2:
        return bin(avg)[2:]
    elif base == 8:
        return oct(avg)[2:]
    elif base == 16:
        return hex(avg)[2:].upper()
    else:
        number_map = (0,1,2,3,4,5,6,7,8,9, 'A','B','C','D','E','F','G','H','I','J')
        res = ''
        while avg:
            avg, idx = divmod(avg, base)
            res = str(number_map[idx]) + res
        return res