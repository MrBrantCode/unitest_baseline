"""
QUESTION:
Write a function `find_second_largest_prime` to find the second largest prime number in an array of positive integers.

The function should take an array of integers as input, where the array contains at least two elements, may contain duplicates, and consists only of positive integers. 

The function should return the second largest prime number in the array.
"""

def find_second_largest_prime(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = 0
    second_max_prime = 0

    for num in arr:
        if is_prime(num):
            if num > max_prime:
                second_max_prime = max_prime
                max_prime = num
            elif num > second_max_prime and num != max_prime:
                second_max_prime = num

    if second_max_prime == 0:
        return "No second largest prime number found."
    else:
        return second_max_prime