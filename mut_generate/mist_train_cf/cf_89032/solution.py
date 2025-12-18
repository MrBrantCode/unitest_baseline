"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of numbers as input. The function should return a list containing only the prime numbers from the input list, sorted in descending order, excluding any prime numbers that contain the digit 7.
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