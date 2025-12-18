"""
QUESTION:
Write a function `generate_and_sort_primes(n)` that generates the first `n` prime numbers and returns them in sorted order. The function should run in O(n log n) time complexity.
"""

def generate_and_sort_primes(n):
    def is_prime(num, primes):
        if num < 2:
            return False
        for prime in primes:
            if num % prime == 0:
                return False
        return True

    def merge_sort(sequence):
        if len(sequence) <= 1:
            return sequence
        else:
            middle = len(sequence) // 2
            left_half = merge_sort(sequence[:middle])
            right_half = merge_sort(sequence[middle:])
            return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left)
        merged.extend(right)
        return merged

    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number, primes):
            primes.append(number)
        number += 1
    return merge_sort(primes)