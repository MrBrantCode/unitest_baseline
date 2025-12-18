"""
QUESTION:
Construct a function named 'weighted_avg_custom_base'. This function should take four arguments: two positive integers 'n' and 'm' where n is less than or equal to m, an integer 'd' such that 1 <= d <= m-n+1, and an integer 'base' ranging from 2 to 20. The function aims to compute the weighted mean of all integers between 'n' and 'm' (inclusive), where the weights of each number are defined by the count of their divisors. The weights are then multiplied by the factor 'd'. The computed weighted mean should be rounded to the closest integer and then converted into a numeral system representation based on the 'base'. If 'n' is more than 'm' or if 'd' and 'base' are not within the stipulated ranges, the function should return -1.
"""

def weighted_avg_custom_base(n, m, d, base):
    """
    This function computes the weighted mean of all integers between 'n' and 'm' (inclusive),
    where the weights of each number are defined by the count of their divisors.
    The weights are then multiplied by the factor 'd'. The computed weighted mean is rounded 
    to the closest integer and then converted into a numeral system representation based on the 'base'.

    Args:
    n (int): The start of the range (inclusive).
    m (int): The end of the range (inclusive).
    d (int): The factor to multiply the weights by.
    base (int): The base of the numeral system.

    Returns:
    str: The weighted mean in the specified numeral system representation.
    """
    
    # Check if inputs are within valid ranges
    if n > m or not 1 <= d <= m - n + 1 or not 2 <= base <= 20:
        return -1
    
    # Initialize sum of weighted numbers and sum of weights
    sum_weighted_num = 0
    sum_weights = 0
    
    # Iterate over the range from n to m
    for num in range(n, m + 1):
        # Calculate the weight (count of divisors)
        weight = sum(1 for i in range(1, num + 1) if num % i == 0)
        
        # Multiply the weight by the factor d
        weighted_num = num * weight * d
        
        # Add to the sum of weighted numbers and sum of weights
        sum_weighted_num += weighted_num
        sum_weights += weight * d
    
    # Calculate the weighted mean
    weighted_mean = round(sum_weighted_num / sum_weights)
    
    # Convert the weighted mean to the specified base
    if base == 2:
        return bin(weighted_mean)
    elif base == 8:
        return oct(weighted_mean)
    elif base == 16:
        return hex(weighted_mean)
    else:
        # Convert to base using standard method
        digits = []
        while weighted_mean > 0:
            digits.append(int(weighted_mean % base))
            weighted_mean //= base
        return str(base) + 'b' + ''.join(map(str, reversed(digits)))