"""
QUESTION:
Write a function `print_prime_descending(numbers)` that prints prime numbers from the given list `numbers` in descending order without using any built-in functions or libraries. The function must implement its own logic to determine if a number is prime or not and must not store the numbers in any additional data structures or arrays, only using a constant amount of extra space. The input list `numbers` can contain up to 1000 elements.
"""

def print_prime_descending(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_num = max(numbers)
    for num in range(max_num, 1, -1):
        if num in numbers and is_prime(num):
            print(num)