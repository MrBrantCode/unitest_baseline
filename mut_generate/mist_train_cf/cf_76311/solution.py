"""
QUESTION:
Design a function `calculate_even_fib_sum(limit)` that calculates the sum of the first `limit` even numbers in the Fibonacci sequence. Use a while loop and memoization to optimize the function's efficacy.
"""

def calculate_even_fib_sum(limit):
    fib_list = {0:0, 1:1} 
    sum_result = 0 
    num = 2  
    even_count = 0 

    while even_count < limit: 
        if num not in fib_list:
            fib_list[num] = fib_list[num-1] + fib_list[num-2] 
        if fib_list[num] % 2 == 0: 
            sum_result += fib_list[num] 
            even_count += 1 
        num += 1 

    return sum_result