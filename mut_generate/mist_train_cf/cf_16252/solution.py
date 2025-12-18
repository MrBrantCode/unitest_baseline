"""
QUESTION:
Write a function `find_largest_prime` that takes a list of positive integers as input and returns the largest prime number in the list. The function should have a time complexity of O(n log log n), where n is the size of the list.
"""

def find_largest_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for num in numbers:
        if largest_prime is None or num > largest_prime:
            if is_prime(num):
                largest_prime = num
    return largest_prime