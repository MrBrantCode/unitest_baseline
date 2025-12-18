"""
QUESTION:
Write a function `separate_numbers(numbers)` that takes a list of integers as input and separates them into three lists: prime numbers, even numbers, and odd numbers. The prime numbers list should be sorted in ascending order.
"""

def separate_numbers(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    evens = []
    odds = []
    
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        elif num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    primes.sort()
    
    return {"Prime numbers": primes, "Even numbers": evens, "Odd numbers": odds}