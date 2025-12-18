"""
QUESTION:
Design a function `fib_product(lst)` that calculates the product of the unique Fibonacci numbers present within the given list `lst`. The function should return the product of unique Fibonacci numbers in `lst` and return 0 if no Fibonacci numbers are present.
"""

def fib_product(lst):
    def is_fib(n):
        if n < 0:
            return False
        x = ((5*(n*n)) - 4)
        y = ((5*(n*n)) + 4)
        
        return (x**0.5).is_integer() or (y**0.5).is_integer()

    unique_fibs = list(set([x for x in lst if is_fib(x)]))
    if len(unique_fibs) == 0: return 0

    product = 1
    for i in unique_fibs:
        product *= i
    return product