"""
QUESTION:
Write a function `filter_list` that takes a list of integers as input. The function should remove any number that is divisible by 7, and for any number that is a prime, add its square to the list. The function should return the resulting list in ascending order. The function should be efficient for large input lists.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_list(numbers):
    result = []
    for num in numbers:
        if num % 7 != 0:
            result.append(num)
            if is_prime(num):
                result.append(num ** 2)
    return sorted(result)