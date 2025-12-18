"""
QUESTION:
Create a function `unique_sum_mult_powers(arr)` that takes an integer array `arr` as input and returns the sum of unique elements raised to their respective absolute values, multiplied by the difference between the count of unique negative elements and the count of unique positive elements. If `arr` is empty, the function should return `None`.
"""

def unique_sum_mult_powers(arr):
    if not arr:
        return None
    
    # get unique values
    c = dict((i, arr.count(i)) for i in arr)  
    unique = list(c.keys())
    
    # count negative and positive values
    neg_count = len([a for a in unique if a < 0])
    pos_count = len([a for a in unique if a > 0])
    
    # calculate the sum of unique values raised to their respective absolute values
    power_sum = sum([abs(a)**abs(a) for a in unique])
    
    # multiply the sum by the unique count of positive and negative elements
    final_result = power_sum * (neg_count - pos_count)
    
    return final_result