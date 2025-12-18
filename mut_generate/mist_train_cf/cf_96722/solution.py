"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the given number `n` and returns the sequence along with the sum of all the Fibonacci numbers up to `n`. The function should take an integer `n` as input and return two values: a list of Fibonacci numbers up to `n` and their sum.
"""

def fibonacci(n):
    sequence = [0, 1]  
    fib_sum = 1  
    
    while sequence[-1] < n:
        next_num = sequence[-1] + sequence[-2]  
        sequence.append(next_num)  
        fib_sum += next_num  
    
    return sequence, fib_sum