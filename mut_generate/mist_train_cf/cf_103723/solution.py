"""
QUESTION:
Write a function `lucas(n)` to find the nth element of the Lucas sequence, where the sequence starts with 2 and 1, and each subsequent number is the sum of the two preceding ones. The function should take an integer `n` as input and return the nth element of the sequence.
"""

def lucas(n):
    # Initialize the first two numbers
    sequence = [2, 1]
    
    # Generate the Lucas sequence up to the nth element
    for i in range(2, n+1):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    # Return the nth element
    return sequence[n-1]