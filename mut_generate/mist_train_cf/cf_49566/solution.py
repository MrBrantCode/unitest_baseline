"""
QUESTION:
Create a function called `lucas_numbers(n)` that generates the first `n` Lucas numbers. The Lucas sequence starts with 2 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def lucas_numbers(n):  
    lucas_series = [2, 1] 
    for i in range(2, n): 
        lucas_series.append(sum(lucas_series[-2:])) 
    return lucas_series 