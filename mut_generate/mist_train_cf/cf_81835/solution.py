"""
QUESTION:
Create a function `fib_sequence_divisible_by(n)` that generates a sequence containing the first 8 Fibonacci numbers divisible by a given positive integer `n`. The function should validate the input and handle any potential errors. The input `n` must be a positive integer, and the function should return an error message if this condition is not met.
"""

def fib_sequence_divisible_by(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer."
        
    fib_seq = [0, 1]
    result = []
    
    while len(result) < 8:     
        new_fib = fib_seq[-2] + fib_seq[-1]
        fib_seq.append(new_fib)
        
        if new_fib % n == 0:
            result.append(new_fib)
   
    return result