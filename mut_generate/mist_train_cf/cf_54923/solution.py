"""
QUESTION:
Create a generator expression that iterates over a list and returns only the prime numbers. The list may contain integers and strings. The generator expression should filter out non-integer values and return prime numbers, considering both integers and strings that can be converted to integers.
"""

def entrance(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return (int(e) for e in lst if (isinstance(e, int) and is_prime(e)) or (isinstance(e, str) and e.isdigit() and is_prime(int(e))))