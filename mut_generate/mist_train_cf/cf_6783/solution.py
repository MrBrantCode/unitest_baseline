"""
QUESTION:
Write a function called `rotate_list` that takes a list of elements and a number `n` as input. The function should rotate the elements in the list to the right by `n` positions, but only if `n` is a prime number. If `n` is not a prime number, return the string "Error: The number of times to rotate must be a prime number." If the input list is empty, return an empty list. The function should be able to handle large lists efficiently.
"""

def rotate_list(lst, n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not lst:
        return []
    if not is_prime(n):
        return "Error: The number of times to rotate must be a prime number."
    n = n % len(lst)
    return lst[-n:] + lst[:-n]