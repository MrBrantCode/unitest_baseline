"""
QUESTION:
Given two containers of books with initial weights A and B in kilograms where A > B, find A and B such that A + B is a prime number. After removing P4 kilograms of books from the larger container, the weight ratio of the remaining books in the larger container (A') to the weight of the books in the smaller container (B) is equal to the ratio of two prime numbers P2 and P3 (P2 > P3), and P4 is also a prime number.
"""

def find_weights(A, B, P2, P3, P4):
    # Check if A + B is a prime number
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(A + B):
        # Check if A' / B equals to the ratio of two prime numbers P2 and P3
        A_prime = A - P4
        if A_prime / B == P2 / P3:
            return A, B, A_prime, P4

    return None