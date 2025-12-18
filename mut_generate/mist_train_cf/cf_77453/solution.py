"""
QUESTION:
Write a function named `ordered_array` that takes an array of integers as input. The function should return a string of comma-separated integers, where the integers are sorted first by their number of divisors in descending order, and then by their numerical value in ascending order if two integers have the same number of divisors.
"""

def ordered_array(arr):
    def divisor_count(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 2 if i != n // i else 1
        return count

    return ','.join(map(str, sorted(arr, key=lambda x: (-divisor_count(x), x))))