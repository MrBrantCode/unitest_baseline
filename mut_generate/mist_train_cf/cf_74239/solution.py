"""
QUESTION:
Implement a function `get_even_prime_tuple_and_merge(l1, l2, l3)` that takes three lists as input and returns a list of tuples. Each tuple must contain two even prime numbers and the resulting list must be sorted in descending order. If a tuple contains at least one non-prime or odd number, it should be excluded from the result. The function should have a helper function `is_prime(n)` to check if a number `n` is prime, and another helper function `merge_and_sort(m, n, o)` to merge and sort the tuples from the input lists.
"""

def get_even_prime_tuple_and_merge(l1, l2, l3):
    """Return only tuples of even prime numbers from all three lists, merged and sorted in descending order."""

    def merge_and_sort(m, n, o):
        return sorted(m + n + o, key=lambda x: (x[0], x[1]), reverse=True)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    l1 = [i for i in l1 if isinstance(i, tuple) and len(i) == 2]
    l2 = [i for i in l2 if isinstance(i, tuple) and len(i) == 2]
    l3 = [i for i in l3 if isinstance(i, tuple) and len(i) == 2]

    even_prime_tuples = [i for i in merge_and_sort(l1, l2, l3) if is_prime(i[0]) and is_prime(i[1]) and i[0] % 2 == 0 and i[1] % 2 == 0]

    return even_prime_tuples