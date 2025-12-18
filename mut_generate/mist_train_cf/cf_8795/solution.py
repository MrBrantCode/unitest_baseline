"""
QUESTION:
Compute the average of a list of numbers, excluding any numbers that are divisible by 5 and contain the digit 7, and also excluding any prime numbers. The function should take a list of integers as input and return the average as a float.

Example input: [45, 20, 15, 100, 75]. The function should not be limited to this specific input and should work with any list of integers.
"""

def entance(lst):
    def is_prime(n):
        """Check if number is prime."""
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

    def has_digit_seven(n):
        """Check if number contains digit 7."""
        return '7' in str(n)

    # Filter out numbers divisible by 5 and contain digit 7, and also prime numbers
    filtered_numbers = [n for n in lst if not (n % 5 == 0 and has_digit_seven(n)) and not is_prime(n)]

    # Calculate and return the average
    if filtered_numbers:
        return sum(filtered_numbers) / len(filtered_numbers)
    else:
        return 0.0