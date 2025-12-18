"""
QUESTION:
Design a function called `Fibonacci(n)` that takes an integer `n` representing the number of digits and returns a Fibonacci sequence where the last number in the sequence has at least `n` digits. The Fibonacci sequence should start with 0 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def entrance(n): 
    sequence = [0, 1]
    
    while len(str(sequence[-1])) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence