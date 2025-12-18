"""
QUESTION:
Write a function called `select_third_largest_prime` that takes in an array `arr`, a minimum range `min_range`, and a maximum range `max_range`. The function should return the third largest unique prime number within the specified range that exists in the array. If there are less than three unique prime numbers within the range, the function should return `None`.
"""

def select_third_largest_prime(arr, min_range, max_range):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    prime_numbers = [num for num in arr if min_range <= num <= max_range and is_prime(num)]
    prime_numbers = list(set(prime_numbers))
    prime_numbers.sort(reverse=True)

    if len(prime_numbers) < 3:
        return None

    return prime_numbers[2]