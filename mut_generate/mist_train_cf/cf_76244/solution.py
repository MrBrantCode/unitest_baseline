"""
QUESTION:
Create a function named `separate_and_sort_numbers` that takes a list of integers as input. Separate the integers into two lists: one for prime numbers and one for composite numbers. Then, sort both lists in descending order and combine them, with the prime numbers first, to produce the final output.
"""

def separate_and_sort_numbers(numbers):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    prime_numbers = [number for number in numbers if is_prime(number)]
    composite_numbers = [number for number in numbers if not is_prime(number)]

    prime_numbers.sort(reverse=True)
    composite_numbers.sort(reverse=True)

    return prime_numbers + composite_numbers