"""
QUESTION:
Create a function named `largest_prime` to find the largest prime number in a given list of positive integers. The function should return -1 if no prime number is found in the list and have a time complexity of O(n√m), where n is the length of the list and m is the largest number in the list.
"""

def largest_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime_number = -1
    for num in numbers:
        if is_prime(num) and num > largest_prime_number:
            largest_prime_number = num
    return largest_prime_number