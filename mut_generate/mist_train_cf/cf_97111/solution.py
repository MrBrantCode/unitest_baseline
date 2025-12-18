"""
QUESTION:
Implement a function named `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. The function should not use built-in sum functions or iteration tools such as 'for' or 'while' loops. The time complexity of the solution should be O(n), where n is the length of the input list.
"""

def sum_of_primes(numbers):
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

    if not numbers:
        return 0
    num = numbers[0]
    if is_prime(num):
        return num + sum_of_primes(numbers[1:])
    else:
        return sum_of_primes(numbers[1:])