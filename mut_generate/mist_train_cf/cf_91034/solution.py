"""
QUESTION:
Write a function named `fibonacci_sequence` that takes two parameters: `n` (the number of Fibonacci numbers to generate) and `k` (the maximum sum of the Fibonacci sequence). The function should generate and return the Fibonacci sequence up to `n` numbers, as well as the sum of the generated Fibonacci numbers. The function should stop generating Fibonacci numbers and return the sequence and sum if the sum of the Fibonacci numbers exceeds `k`.
"""

def fibonacci_sequence(n, k):
    sequence = []
    sum_of_fibonacci = 0
    
    a, b = 0, 1
    
    for i in range(n):
        sequence.append(b)
        sum_of_fibonacci += b
        
        if sum_of_fibonacci > k:
            break
        
        a, b = b, a + b
    
    return sequence, sum_of_fibonacci