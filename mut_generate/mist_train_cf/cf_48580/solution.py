"""
QUESTION:
Write a function named `rounded_avg_custom_base` that takes four parameters: two integers `n` and `m` where `n` is less than or equal to `m`, an integer `base` between 2 and 10 (inclusive), and an integer `limit`. The function should calculate the weighted median of integers from `n` to `m` (inclusive) based on their divisor counts, use this median as an argument for an arithmetic sequence, calculate the sum of the sequence up to the given `limit`, and convert this sum to the given `base`. If `n` is greater than `m` or `base` is outside the accepted range, return -1.
"""

def rounded_avg_custom_base(n, m, base, limit): 
    # Validate inputs
    if not (2 <= base <= 10) or n > m: 
        return -1
    
    def divisor_count(n): 
        # Get divisors for a number
        count = 2  #1 and n are always divisors
        i = 2 
        while i * i <= n: 
            if n % i: 
                i += 1
            else: 
                if n == i * i: 
                    count += 1 
                else: 
                    count += 2
                n /= i
        return count

    def base_convert(n, base): 
        # Function to convert to any base
        convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while n > 0: 
            result = convertString[n % base] + result
            n = n // base
        return result

    def weighted_median(sorted_nums, weights): 
        # Calculate the weighted median
        n = sum(weights)
        midpoint = 0.5 * n
        accum = weights[0]
        
        for i, weight in enumerate(weights[1:], start=1): 
            if accum < midpoint <= (accum + weight): 
                return sorted_nums[i]
            accum += weight

    # Compute divisor counts
    nums = list(range(n, m + 1))
    counts = [divisor_count(num) for num in nums]
    
    # Compute weights
    counts_sum = sum(counts)
    weights = [count / counts_sum for count in counts]
    
    # Compute weighted median and convert it to the base
    med = weighted_median(nums, weights)
    
    # The sum of the arithmetic sequence: a + (n-1)d/2 * n
    sum_seq = (med * (med - 1)) / 2 * med
    
    if sum_seq > limit: 
        return -1
    
    return base_convert(int(sum_seq), base)