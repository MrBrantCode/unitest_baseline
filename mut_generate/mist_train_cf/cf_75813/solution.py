"""
QUESTION:
Write a function `primeWithPrimeDigitSum(lst)` that receives a list of integers `lst` and returns a tuple containing the largest prime number in `lst` whose digits sum up to another prime number and the sum of its digits. If no such prime number is found, return `None`.
"""

def isprime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def digitSum(n):
    digitSum = 0
    while n:
        digitSum += n % 10
        n //= 10
    return digitSum

def primeWithPrimeDigitSum(lst):
    maxPrime = 0
    sumDigits = 0
    for i in lst:
        if isprime(i):
            digit_sum = digitSum(i)
            if isprime(digit_sum) and i > maxPrime:
                maxPrime = i
                sumDigits = digit_sum
    if maxPrime == 0:
        return None
    else:
        return (maxPrime, sumDigits)