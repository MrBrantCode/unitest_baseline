"""
QUESTION:
Write a function `fibo_gcd(n)` that generates the Fibonacci sequence up to the nth number and calculates the greatest common divisor (GCD) of every pair of adjacent Fibonacci numbers. The function should return a list of these GCDs. Ensure the runtime complexity does not exceed O(n * log n).
"""

def fibo_gcd(n):
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    fibNumbers = [0, 1]
    for i in range(2, n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])

    gcdPairs = []
    for i in range(1, n):
        gcdPairs.append(gcd(fibNumbers[i-1], fibNumbers[i]))
    
    return gcdPairs