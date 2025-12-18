"""
QUESTION:
Design a function `classify` that takes a list of integers as input and returns four lists: even, odd, prime, and composite numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A composite number is a positive integer that has at least one positive divisor other than 1 and itself. The function should categorize the input integers into these four categories.
"""

def classify(numbers):
    """
    Classify a list of integers into four categories: even, odd, prime, and composite numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple of four lists: even, odd, prime, and composite numbers.
    """
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    prime = [num for num in numbers if check_prime(num)]
    composite = [num for num in numbers if num > 1 and not check_prime(num)]

    return even, odd, prime, composite