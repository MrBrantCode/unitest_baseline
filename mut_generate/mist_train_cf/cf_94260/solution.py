"""
QUESTION:
Implement a function `remove_divisible_not_prime(lst)` that takes a list of integers as input and returns the modified list with all elements that are divisible by 4 and not prime numbers removed. The function should have a time complexity of O(n) and a space complexity of O(1). Do not use any built-in libraries or functions for checking prime numbers.
"""

def remove_divisible_not_prime(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    i = 0
    j = 0
    while i < len(lst):
        if lst[i] % 4 == 0 and not is_prime(lst[i]):
            i += 1
        else:
            lst[j] = lst[i]
            i += 1
            j += 1
    return lst[:j]