"""
QUESTION:
Write a function named `find_max_prime_with_repeated_digit` that takes an array of integers as input and returns the maximum prime number in the array that has at least one repeated digit and the sum of its digits is divisible by 3. If no such prime number is found, the function should return -1.
"""

def find_max_prime_with_repeated_digit(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = -1
    for num in arr:
        if is_prime(num) and len(set(str(num))) < len(str(num)) and sum(int(digit) for digit in str(num)) % 3 == 0:
            max_prime = max(max_prime, num)
    return max_prime