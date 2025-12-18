"""
QUESTION:
Write a function named `fibonacci_sequence` that takes two parameters, `n` and `k`, where `n` is the maximum number of Fibonacci numbers to generate and `k` is the threshold sum. The function should generate the Fibonacci sequence up to `n` numbers, calculate the sum of these numbers, and stop generating more numbers if the sum exceeds `k`. The function should return the generated Fibonacci sequence and the sum of the numbers in the sequence.
"""

def fibonacci_sequence(n, k):
    sequence = []
    sum_of_fibonacci = 0
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    for i in range(n):
        # Add the current Fibonacci number to the sequence
        sequence.append(b)
        
        # Update the sum of Fibonacci numbers
        sum_of_fibonacci += b
        
        # Check if the sum exceeds the threshold
        if sum_of_fibonacci > k:
            break
        
        # Calculate the next Fibonacci number
        a, b = b, a + b
    
    return sequence, sum_of_fibonacci