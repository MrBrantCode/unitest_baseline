"""
QUESTION:
Write a function `bitwise_division(N, M)` that takes two positive integers N (1 ≤ N ≤ 10^9) and M (1 ≤ M ≤ 10^9) as input, and returns the quotient of N divided by M without using the division operator (/) or the modulo operator (%). The function should use only bitwise operators.
"""

def bitwise_division(N, M):
    quotient = 0
    
    # Iterate from the MSB to the LSB of N
    for i in range(31, -1, -1):
        quotient = quotient << 1  # Shift the quotient one position to the left
        
        if (N - (M << i)) >= 0:  
            N -= M << i
            quotient += 1
    
    return quotient