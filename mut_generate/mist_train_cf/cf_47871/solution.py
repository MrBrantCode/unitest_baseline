"""
QUESTION:
Write a function named `sort_array(arr)` that takes a list of integers as input, and returns a new list where all prime numbers from the input list are at the beginning, maintaining their original order, followed by the non-prime numbers.
"""

def sort_array(arr):
    def check_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i) <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime = []
    non_prime = []
    for num in arr:
        if check_prime(num):
            prime.append(num)
        else:
            non_prime.append(num)
    return prime + non_prime