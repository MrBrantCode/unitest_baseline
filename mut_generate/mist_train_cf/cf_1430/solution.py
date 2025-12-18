"""
QUESTION:
Create a function named `print_pyramid` that takes an integer `height` as input and prints out a pyramid of stars with the given height. The height must be a prime number between 1 and 100. If the height is not prime, the function should print an error message instead of the pyramid. The function should handle the case where the input height is not a prime number, but it does not need to handle cases where the input is not an integer or outside the range of 1 to 100.
"""

def print_pyramid(height):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(height):
        print("Height must be a prime number between 1 and 100.")
        return

    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))