"""
QUESTION:
Create a function called `lucas_sequence` that generates the nth number in the Lucas sequence, where the Lucas sequence is defined as L(n) = L(n-1) + L(n-2), L(0) = 2, and L(1) = 1. The function should take an integer `n` as input and return the corresponding Lucas number.
"""

def lucas_sequence(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        lucas_numbers = [2, 1]
        for i in range(2, n+1):
            lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])
        return lucas_numbers[-1]