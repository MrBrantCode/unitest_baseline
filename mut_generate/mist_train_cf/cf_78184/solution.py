"""
QUESTION:
Create a function `unique_powers_sum_and_mult(arr, p, q)` that takes an array of integers `arr` and two integer parameters `p` and `q` as input. The function should calculate the sum of unique positive integers in `arr` raised to the power `p` and unique negative integers raised to the power `q`, then multiply these sums by the count of unique positive and negative integers, respectively. If `arr` is empty, the function should return `None`.
"""

def unique_powers_sum_and_mult(arr, p, q):
    """
    Calculate the sum of unique positive integers raised to the power p and 
    unique negative integers raised to the power q, then multiply these sums 
    by the count of unique positive and negative integers, respectively.
    
    Args:
    arr (list): A list of integers.
    p (int): The power for positive integers.
    q (int): The power for negative integers.
    
    Returns:
    int or None: The result of the calculation or None if arr is empty.
    """
    if not arr:
        return None

    unique_pos, unique_neg = set(), set()
    for num in arr:           
        if num > 0:  
            unique_pos.add(num)
        elif num < 0:                 
            unique_neg.add(num)

    pos_sum = sum(element**p for element in unique_pos)
    neg_sum = sum(element**q for element in unique_neg)
    
    return pos_sum * len(unique_pos) + neg_sum * len(unique_neg)