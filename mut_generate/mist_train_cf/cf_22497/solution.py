"""
QUESTION:
Implement a function called `sum_of_primes` that takes in a list of integers and returns the sum of all prime numbers in the list. The solution should not use built-in functions like `sum` or iteration tools like `for` or `while` loops, and should achieve a time complexity of O(n), where n is the length of the input list. The input list is assumed to only contain integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(numbers):
    if not numbers:
        return 0
    num = numbers[0]
    if is_prime(num):
        return num + sum_of_primes(numbers[1:])
    else:
        return sum_of_primes(numbers[1:])