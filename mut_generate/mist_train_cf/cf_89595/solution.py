"""
QUESTION:
Rotate the elements in the given list by a certain number of times using the function `rotate_list(lst, n)`, where `n` is a prime number. If `n` is not a prime number, return "Error: The number of times to rotate must be a prime number." If the input list is empty, return an empty list. The function should handle cases where `n` is larger than the length of the list efficiently.
"""

def rotate_list(lst, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not lst:
        return []
    if not is_prime(n):
        return "Error: The number of times to rotate must be a prime number."
    n = n % len(lst)
    return lst[n:] + lst[:n]