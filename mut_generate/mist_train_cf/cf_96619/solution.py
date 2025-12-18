"""
QUESTION:
Generate a function called `generate_fibonacci` that returns an array of the next n numbers in the Fibonacci sequence, excluding any numbers that are divisible by 3 or 5. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def generate_fibonacci(n):
    fibonacci = []
    a, b, c = 0, 1, 1
    
    while len(fibonacci) < n:
        if c % 3 != 0 and c % 5 != 0:
            fibonacci.append(c)
        
        a, b, c = b, c, b + c
    
    return fibonacci