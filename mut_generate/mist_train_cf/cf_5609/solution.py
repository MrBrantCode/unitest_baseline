"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list that do not contain the digit 7, sorted in descending order.
"""

def get_prime_numbers(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def contains_digit_seven(num):
        return '7' in str(num)

    prime_numbers = [num for num in numbers if is_prime(num) and not contains_digit_seven(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers