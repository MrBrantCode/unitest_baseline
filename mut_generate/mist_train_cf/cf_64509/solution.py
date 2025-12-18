"""
QUESTION:
Create a function called `reverse_fibonacci(n)` that generates the first `n` Fibonacci numbers, reverses the order of the sequence, and returns the result. The function should have a time complexity of O(n) or less and include exception handling to catch any potential errors.
"""

def reverse_fibonacci(n):
    try:
        fib = [0] * n
  
        # assigning first and second elements
        fib[0] = 0
        fib[1] = 1
  
        # Fibonacci calculation
        for i in range(2, n): 
            fib[i] = fib[i - 1] + fib[i - 2] 
  
        fib = fib[::-1]  # list reversed
  
        return fib
    except Exception as e:  # Exception handling
        print(f"An error occurred: {e}")