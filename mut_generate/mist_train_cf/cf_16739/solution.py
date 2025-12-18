"""
QUESTION:
Generate a function `generate_prime_numbers` to find 5 random prime numbers between 1000 and 10000, such that the sum of the digits of each prime number is also a prime number.
"""

def generate_prime_numbers(start, end, count):
    """
    Generate a specified number of prime numbers within a given range where the sum of the digits of each prime number is also a prime number.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
        count (int): The number of prime numbers to generate.

    Returns:
        list: A list of prime numbers.
    """
    
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        """Calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))

    prime_numbers = []
    num = start
    while len(prime_numbers) < count:
        if is_prime(num) and is_prime(sum_of_digits(num)):
            prime_numbers.append(num)
        num += 1
        if num > end:
            break

    return prime_numbers

# Example usage: print(generate_prime_numbers(1000, 10000, 5))