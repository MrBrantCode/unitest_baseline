"""
QUESTION:
Write a function `nth_prime(n)` to find the nth prime number. The function takes an integer `n` as input and returns the corresponding nth prime number. The function should handle the case when `n` is 0 by returning `None`.
"""

def nth_prime(n):
    if n == 0:
        return None
    
    primeCount = 0
    checkNum = 2
    while(primeCount < n):
        isPrime = True
        for i in range(2, checkNum):
            if checkNum % i == 0:
                isPrime = False
        
        if isPrime == True:
            primeCount += 1
        
        if primeCount == n:
            return checkNum
        else:
            checkNum += 1