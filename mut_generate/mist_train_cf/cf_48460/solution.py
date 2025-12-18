"""
QUESTION:
Create a function `digits_bounded_by_primes` that takes a series of alphanumeric symbols as input and returns a list of position indexes of decimal digits that are surrounded by prime numbers on either side, excluding the first and last digit of the series. The index is 0-based and is with respect to the filtered series after removing non-digits. If no such digits are found, return an empty list. The function should disregard any non-digit symbols and handle sequences of varying lengths and complexities.
"""

def digits_bounded_by_primes(series):
    def is_prime(n):
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    series = ''.join(filter(str.isdigit, series)) # remove non-digits
    indexes = []
    for i in range(1, len(series) - 1):
        left_num, target_num, right_num = map(int, series[i-1:i+2])
        if is_prime(left_num) and is_prime(right_num):
            indexes.append(i)
    return indexes if indexes else []