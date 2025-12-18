"""
QUESTION:
Create a function `check_number` that takes an integer `number`, an optional base `base` (defaulting to 10), and an optional divisor `divisor` (defaulting to None), and returns a tuple containing the original number, its base, whether it is a palindrome, whether it is a prime number, and whether it is divisible by the specific divisor. Implement the function to handle input in different bases, such as binary or hexadecimal, and large integers with up to 1000 digits. The function should be optimized for time complexity. Additionally, create a function `print_table` that takes a list of numbers, a base, and a divisor, and prints a LaTeX table with the results of the checks for each number.
"""

def check_number(number, base=10, divisor=None):
    def is_palindrome(n, base):
        if base == 10:
            number_str = str(n)
        else:
            number_str = hex(n)[2:] if base == 16 else bin(n)[2:]
        return number_str == number_str[::-1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_divisible(n, divisor):
        return n % divisor == 0 if divisor else None

    palindrome = is_palindrome(number, base)
    prime = is_prime(number)
    divisible = is_divisible(number, divisor)
    return (number, base, palindrome, prime, divisible)