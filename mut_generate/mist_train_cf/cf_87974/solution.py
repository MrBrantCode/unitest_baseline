"""
QUESTION:
Write a function `longest_consecutive_sequence(arr)` that takes an array of integers as input and returns the length of the longest consecutive sequence of prime numbers that are also perfect squares and have a digit sum that is divisible by 3. The sequence must be consecutive in terms of the array's elements, not necessarily in terms of numerical value.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def longest_consecutive_sequence(arr):
    longest_sequence = 0

    for num in arr:
        if math.isqrt(num) ** 2 == num and is_prime(num) and sum(map(int, str(num))) % 3 == 0:
            current_sequence = 1
            next_num = num + 1

            while next_num in arr and math.isqrt(next_num) ** 2 == next_num and is_prime(next_num) and sum(map(int, str(next_num))) % 3 == 0:
                current_sequence += 1
                next_num += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence