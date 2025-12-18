"""
QUESTION:
Write a function `print_prime_numbers(numbers)` that takes a list of integers as input and prints the prime numbers in the list in ascending order. The function should also print the product of all the prime numbers in the list. Do not use any built-in functions, methods, loops, or recursion in your solution.
"""

def print_prime_numbers(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in numbers if is_prime(num)]
    product = 1
    for num in prime_numbers:
        product *= num

    print('\n'.join(map(str, sorted(prime_numbers))))
    print("The product of the prime numbers is:", product)