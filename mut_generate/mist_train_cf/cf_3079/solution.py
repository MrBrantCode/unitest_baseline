"""
QUESTION:
Write a function called `select_third_largest_prime` that takes in an array `arr`, a minimum range `min_range`, and a maximum range `max_range`. The function should select the third largest unique prime number within the specified range in the array.
"""

def select_third_largest_prime(arr, min_range, max_range):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    prime_numbers = [num for num in set(range(min_range, max_range + 1)) if is_prime(num)]
    prime_numbers.sort(reverse=True)

    return prime_numbers[2] if len(prime_numbers) >= 3 else None