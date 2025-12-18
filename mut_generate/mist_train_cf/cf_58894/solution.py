"""
QUESTION:
Write a function `multiply_fibonacci(M, P)` that takes two integers `M` and `P` as arguments. The function should calculate the multiplication result of all Fibonacci sequence numbers ranging between 0 and `M` that exclusively exceed the value of `P`. Return the multiplication result. The function should only consider Fibonacci numbers that are greater than `P`, and the Fibonacci sequence should only be generated up to `M`.
"""

def multiply_fibonacci(M, P):
    # Initialize Fibonacci sequence
    fib = [0, 1]
    
    # Generate Fibonacci sequence up to M
    while fib[-1] + fib[-2] <= M:
        fib.append(fib[-1] + fib[-2])
      
    # Find Fibonacci numbers greater than P and multiply them
    result = 1
    for num in fib:
        if num > P:
            result *= num
            
    return result