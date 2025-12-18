"""
QUESTION:
Write a function named `generate_odd_fibonacci` that generates an array containing the first `n` odd Fibonacci numbers greater than 1000. The function should take an integer `n` as input and return a list of integers.
"""

def generate_odd_fibonacci(n):
    fibonacci = [1, 1]  
    odd_fibonacci = []  

    while len(odd_fibonacci) < n:
        next_fibonacci = fibonacci[-1] + fibonacci[-2]
        if next_fibonacci % 2 != 0 and next_fibonacci > 1000:
            odd_fibonacci.append(next_fibonacci)
        fibonacci.append(next_fibonacci)
    
    return odd_fibonacci