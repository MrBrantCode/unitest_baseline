"""
QUESTION:
Write a function `evenFibonacciSum(limit)` that calculates the sum of all the even Fibonacci numbers less than or equal to the given integer `limit`. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def entrance(limit):
    fib_sequence = [0, 1]
    even_sum = 0
    
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > limit:
            break
        fib_sequence.append(next_fib)
    
    for num in fib_sequence:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum