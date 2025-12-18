"""
QUESTION:
Implement the function named "weighted_avg_divisor_count_power_base":

This function takes four integral positive values: a range defined by 'n' and 'm' (n <= m), a base (2 <= base <= 20), and a power 'k' (1 <= k <= 10). It calculates the weighted mean of the integers within the given range, where the weights are the count of their divisors raised to the power 'k'. The function then rounds the resulting average to the nearest integer and converts it to the custom numbering system specified by 'base'. If 'n' is greater than 'm', or 'base' and 'k' don't meet the conditions, the function returns -1.
"""

def weighted_avg_divisor_count_power_base(n, m, base, k):
    """
    This function calculates the weighted mean of the integers within the given range, 
    where the weights are the count of their divisors raised to the power 'k'. 
    The function then rounds the resulting average to the nearest integer and converts 
    it to the custom numbering system specified by 'base'. 
    If 'n' is greater than 'm', or 'base' and 'k' don't meet the conditions, 
    the function returns -1.
    """
    
    # Check if n is greater than m, or base and k don't meet the conditions
    if n > m or not (2 <= base <= 20 and 1 <= k <= 10):
        return -1
    
    # Initialize sum of weighted numbers and sum of weights
    sum_weighted = 0
    sum_weights = 0
    
    # Iterate over the range from n to m (inclusive)
    for num in range(n, m + 1):
        # Count the divisors of the current number
        count_divisors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count_divisors += 1
        
        # Calculate the weight for the current number
        weight = count_divisors ** k
        
        # Add the weighted number to the sum
        sum_weighted += num * weight
        
        # Add the weight to the sum of weights
        sum_weights += weight
    
    # Calculate the weighted mean
    weighted_mean = sum_weighted / sum_weights
    
    # Round the weighted mean to the nearest integer
    weighted_mean = round(weighted_mean)
    
    # Convert the weighted mean to the specified base
    if base == 2:
        result = "0b" + bin(weighted_mean)[2:]
    elif base == 8:
        result = "0o" + oct(weighted_mean)[2:]
    elif base == 16:
        result = "0x" + hex(weighted_mean)[2:]
    else:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while weighted_mean > 0:
            result = digits[weighted_mean % base] + result
            weighted_mean //= base
    
    return result