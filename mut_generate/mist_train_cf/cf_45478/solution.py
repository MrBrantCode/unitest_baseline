"""
QUESTION:
Create a function named `segregate_numbers` that takes a list of integers as input and returns two lists. The first list should contain numbers that are part of the Fibonacci sequence, and the second list should contain numbers that are not part of the Fibonacci sequence. Assume that the input list only contains non-negative integers.
"""

def segregate_numbers(lst):
    def fib_check(n):
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            a, b = 1, 1
            while b < n:
                a, b = b, a+b
            return b == n

    fib_numbers = []
    non_fib_numbers = []
    
    for num in lst:
        if fib_check(num):
            fib_numbers.append(num)
        else:
            non_fib_numbers.append(num)
            
    return fib_numbers, non_fib_numbers