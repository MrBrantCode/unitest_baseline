"""
QUESTION:
Calculate the total quantity of numbers that possess non-repeating digits within the constraints of `0 <= x < 10^n`, given an integer `n` where `0 <= n <= 10`.
"""

def findNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    
    base = 9
    count = 10 # for n = 1
    
    for i in range(2, n+1):
        base *= (10-i+1)
        count += base
        
    return count