"""
QUESTION:
Create a function `analyze_numbers` that takes a list of integers as input. For each number in the list, the function should determine whether it is even or odd and whether it is a prime number or not, then print out the corresponding result.
"""

def analyze_numbers(numbers):
    """Analyze a list of numbers and print whether each number is even or odd, and whether it is a prime number or not."""
    def is_prime(n):
        """Return whether a number is a prime number or not."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in numbers:
        # Determine if the number is even or odd
        if number % 2 == 0:
            print(f'{number} is even, ', end='')
        else:
            print(f'{number} is odd, ', end='')

        # Determine if the number is prime
        if is_prime(number):
            print('prime number.')
        else:
            print('not a prime number.')