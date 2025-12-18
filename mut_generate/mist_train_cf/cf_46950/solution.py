"""
QUESTION:
Write a function `count_active_bits_in_prime_elements(binary)` that takes a binary numeral as input and returns the count of active bits located in its prime elements. The function should work by first converting the binary numeral to a decimal, then checking each number from 2 to the decimal number to see if it is prime, and finally counting the number of active bits in the binary representation of the prime numbers. The input binary is a string of '0's and '1's, and the output is an integer.
"""

def entance(binary):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            return False
        return True

    number = int(binary, 2)
    return sum(bin(i).count('1') for i in range(2, number + 1) if is_prime(i))