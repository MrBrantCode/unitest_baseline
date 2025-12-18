"""
QUESTION:
Create a function named `count_ways` that takes an integer `n` as input, representing the number of stairs, and returns the number of different ways to climb these stairs, where you can climb 1, 2, or 3 stairs at a time.
"""

def count_ways(n): 
    if n==1 or n==0: 
        return 1
    elif n==2: 
        return 2
    else: 
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)