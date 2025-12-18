"""
QUESTION:
Write a function named `generate_fibonacci` that takes an integer `n` as input and returns an array of the first `n` Fibonacci numbers. The function should have a time complexity of O(n).
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci = [0, 1]  
    
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])  
    
    return fibonacci