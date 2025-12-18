"""
QUESTION:
Write a function named `print_prime_numbers` that takes a list of integers as input and prints out the prime numbers from the list in ascending order. Additionally, the function should print the product of all the prime numbers found. The function should not use any built-in functions or methods, and it should not use loops or recursion to achieve this. However, helper functions are allowed.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    product = 1
    for num in sorted(prime_numbers):
        print(num)
        product *= num

    print("The product of the prime numbers is:", product)