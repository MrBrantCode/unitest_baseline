"""
QUESTION:
Create a function called `printPrimes` that takes two integer parameters `start` and `end` and prints all prime numbers between `start` and `end` (inclusive) in increasing order using a recursive approach. The function should check each number in the range to see if it is prime by calling a helper function `isPrime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is prime. The `isPrime` function should check if `n` is less than 2 or divisible evenly by any number between 2 and the square root of `n`. If `n` is not divisible evenly by any number, it is prime.
"""

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def printPrimes(start, end):
    if start > end:
        return
    if isPrime(start):
        print(start)
    printPrimes(start + 1, end)