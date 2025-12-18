"""
QUESTION:
Write a function named `power_of_2(n)` that takes an integer `n` as input and returns a list of all powers of 2 less than or equal to `n`.
"""

def power_of_2(n): 
    res = []
    for i in range(n+1):
        if i & (i-1) == 0 and i != 0:
            res.append(i)
        
    return res