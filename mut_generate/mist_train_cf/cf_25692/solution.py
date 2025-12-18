"""
QUESTION:
Write a function `findNumbers(N, M)` to find the count of numbers from 1 to N (inclusive) where the last digit is less than or equal to M.
"""

def findNumbers(N, M): 
    count = 0
    for i in range(1, N+1): 
        if i % 10 <= M: 
            count += 1
    return count