"""
QUESTION:
Write a function named sum_odd_numbers that calculates the sum of all odd numbers from 1 to n (inclusive) using a while loop, where n is a given integer. The function should return the sum of these odd numbers.
"""

def sum_odd_numbers(n):
    total_sum = 0
    num = 1
    
    while num <= n:
        if num % 2 != 0:
            total_sum += num
        num += 1
        
    return total_sum