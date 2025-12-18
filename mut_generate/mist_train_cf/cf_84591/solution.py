"""
QUESTION:
Write a function named `weighted_median_custom_base` that takes three integers `n`, `m`, and `base` as input, where `n` and `m` are positive integers with `n <= m` and `base` is an integer within the range [3, 12]. The function should calculate the weighted median of the integers from `n` to `m` (inclusive) using their factors' sum as weights, round the median to the closest integer, and convert it to the custom base system specified by `base`. If `n` exceeds `m` or `base` is not within the permissible range, return -1.
"""

def weighted_median_custom_base(n, m, base):
    if n > m or base not in range(3, 13):
        return -1
    else:
        factor_sums, nums = [], []
        for i in range(n, m+1):
            factor_sum = sum([j for j in range(1, i+1) if i%j == 0])
            factor_sums.append(factor_sum)
            nums.append(i)
        weights = [i/sum(factor_sums) for i in factor_sums]
        weighted_nums = [nums[i]*weights[i] for i in range(len(nums))]
        median = round(sum(weighted_nums))
        
        # convert to desired base
        convertString = "0123456789ABC"
        if median == 0:
            return '0'
        result = ''
        while median > 0:
            result = convertString[median % base] + result
            median = median // base
        return result