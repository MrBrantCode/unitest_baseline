"""
QUESTION:
Create a function called `find_prime_in_range` that takes two parameters, `low` and `high`, representing the range of numbers to search for a prime. The function should find and return a prime number within the given range using a search algorithm with a time complexity not exceeding O(log n). The function should return -1 if no prime number is found.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_prime_in_range(low, high):
    while low <= high:
        mid = (low + high) // 2
        if is_prime(mid):
            return mid

        if is_prime(mid - 1):
            return mid - 1
        elif is_prime(mid + 1):
            return mid + 1

        if mid % 2 == 0:
            low = mid + 1
        else:
            high = mid - 1

    return -1