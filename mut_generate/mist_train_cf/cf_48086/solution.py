"""
QUESTION:
Write a Python function `harmonic_mean(a, b, c)` that calculates the harmonic mean of three numbers `a`, `b`, and `c`, with the restriction that none of the inputs can be zero.
"""

def harmonic_mean(a, b, c):
    # Checks if any of the inputs is zero to avoid divide by zero error
    if a==0 or b==0 or c==0:
        return "Error: Divide by zero"
    
    return 3/(1/a + 1/b + 1/c)