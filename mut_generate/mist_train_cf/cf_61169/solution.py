"""
QUESTION:
Write a function `prime_numbers(start, end)` that generates a list of all the prime numbers between two given numbers `start` and `end` (inclusive), where `start` and `end` are integers and `start` is less than or equal to `end`. The function should return a list of integers.
"""

def entrance(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  
            for i in range(2, num):
                if (num % i) == 0:  
                    break
            else:
                primes.append(num)  
    return primes