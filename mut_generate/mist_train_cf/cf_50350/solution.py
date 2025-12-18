"""
QUESTION:
Write a function `starts_one_ends(n, x, y)` that accepts a positive whole number `n` and two non-negative integers `x` and `y`. The function should return the total count of `n`-digit numbers that begin and end with digit `1`, are divisible by both `3` and `5`, and do not contain the digits `x` or `y`. The input `n` is guaranteed to be greater than `1`.
"""

def starts_one_ends(n, x, y):
    if n < 2:
        return 0
    
    count = 0
    unwanted_digits = set(str(x) + str(y))
    
    upper_limit = 10**n    
    step = 3 * 5  # for numbers to be divisible by both 3 & 5, they should be divisible by their LCM that is, 15
   
    for num in range(10**(n-1), upper_limit, step):  
        str_num = str(num)
        if str_num[0] == str_num[-1] == '1' and not any(digit in unwanted_digits for digit in str_num):
            count += 1

    return count