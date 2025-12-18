"""
QUESTION:
Create a function named `process_list` that takes a list of integers as input and returns a sorted list in ascending order with no duplicates. For each input element, if it is a prime number, cube the number; otherwise, triple the number.
"""

def process_list(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    return sorted([num**3 if is_prime(num) else num*3 for num in set(lst)])