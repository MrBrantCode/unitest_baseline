"""
QUESTION:
Write a function `sum_elements_fibonacci(a)` that determines if a given integer `a` (where `a` is less than 1000) can be represented as the sum of three consecutive Fibonacci numbers. Return `True` if such a representation exists and `False` otherwise.
"""

def sum_elements_fibonacci(a):
    fib_list = [0, 1]
    while fib_list[-1] < a:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    for i in range(len(fib_list)-2):
        if fib_list[i] + fib_list[i+1] + fib_list[i+2] == a:
            return True
    return False