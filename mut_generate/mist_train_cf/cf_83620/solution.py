"""
QUESTION:
Write a function named `starts_ends_seven(n)` that computes the sum of all n-digit positive integers that start or end with 7, are divisible by 2, 3, or 7, but are excluded if they are divisible by both 3 and 7 unless they are also divisible by 21.
"""

from itertools import product

def starts_ends_seven(n):
    pool = [str(i) for i in range(10)]
    sum_result = 0
    for combination in product(pool, repeat=n):
        num_str = ''.join(combination)
        num = int(num_str)
        if num % 2 == 0 or num % 3 == 0 or num % 7 == 0: 
            if (num % 3 == 0 and num % 7 == 0) and num % 21 != 0: 
                continue
            if num_str.startswith('7') or num_str.endswith('7'):  
                sum_result += num
        
    return sum_result