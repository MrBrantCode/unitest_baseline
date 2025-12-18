"""
QUESTION:
# Task
 The number is considered to be `unlucky` if it does not have digits `4` and `7` and is divisible by `13`. Please count all unlucky numbers not greater than `n`.

# Example

 For `n = 20`, the result should be `2` (numbers `0 and 13`).
 
 For `n = 100`, the result should be `7` (numbers `0, 13, 26, 39, 52, 65, and 91`)
 
# Input/Output


 - `[input]` integer `n`

 `1 ≤ n ≤ 10^8(10^6 in Python)`


 - `[output]` an integer
"""

def count_unlucky_numbers(n):
    """
    Counts the number of unlucky numbers not greater than `n`.
    
    An unlucky number is defined as a number that:
    1. Does not contain the digits '4' or '7'.
    2. Is divisible by 13.
    
    Parameters:
    - n (int): The upper limit (inclusive) up to which to count the unlucky numbers.
    
    Returns:
    - int: The count of unlucky numbers not greater than `n`.
    """
    return sum((not ('4' in s or '7' in s) for s in map(str, range(0, n + 1, 13))))