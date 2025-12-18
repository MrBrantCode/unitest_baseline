"""
QUESTION:
Design a function named `separate_numbers` that takes a list of integers as input and returns a tuple of three lists: prime numbers, even numbers, and odd numbers. The function should correctly identify prime numbers, even numbers, and odd numbers from the input list and return them in three separate lists.
"""

def separate_numbers(numbers):
    primes = []
    evens = []
    odds = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return (primes, evens, odds)