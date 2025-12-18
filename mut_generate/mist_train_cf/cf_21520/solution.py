"""
QUESTION:
Write a function named `generate_fibonacci(n)` that generates the next n numbers in the Fibonacci sequence, excluding any numbers that are divisible by 3 or 5. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of Fibonacci numbers to generate.
"""

def generate_fibonacci(n):
    fibonacci = []
    a, b, c = 0, 1, 1
    
    while len(fibonacci) < n:
        if c % 3 != 0 and c % 5 != 0:
            fibonacci.append(c)
        
        a, b, c = b, c, b + c
    
    return fibonacci