"""
QUESTION:
Create a function called `reverse_array` that takes an array of integers as input and returns the reversed array with no duplicates and no prime numbers, preserving the original order of non-duplicate, non-prime elements. The input array can contain negative numbers and the function should handle this case.
"""

def reverse_array(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    seen = set()
    reversed_arr = []
    for x in arr[::-1]:
        if x not in seen and not is_prime(x):
            reversed_arr.append(x)
            seen.add(x)
    return reversed_arr