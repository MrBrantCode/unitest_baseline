"""
QUESTION:
Write a function `generate_factorials(n)` that generates all factorial numbers from 1 to n. The function should be optimized to handle large inputs efficiently (up to n = 10^9) and should return an error message for negative input values of n.
"""

def generate_factorials(n):
    if n < 0:
        return "Error: Negative input"
    
    factorials = [1] * (n + 1)
    
    for i in range(2, n + 1):
        factorials[i] = (factorials[i - 1] * i) % (10 ** 9 + 7)  
    
    return factorials[1:]