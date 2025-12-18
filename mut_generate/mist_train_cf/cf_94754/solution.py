"""
QUESTION:
Create a function `reverse_and_remove_duplicates` that takes an array of integers as input and returns two values: 
- The reversed array with duplicates removed and all prime numbers excluded, preserving the original order.
- A dictionary where keys are non-prime numbers from the reversed array and values are their corresponding counts.

The input array may contain negative numbers, but the function should only consider the absolute values when checking for primes.
"""

def reverse_and_remove_duplicates(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(abs(num)**0.5) + 1):
            if num % i == 0:
                return False
        return True

    reversed_arr = arr[::-1]
    non_prime_count = {}

    for num in reversed_arr[:]:
        if is_prime(abs(num)):
            reversed_arr.remove(num)
        elif num not in non_prime_count:
            non_prime_count[num] = 1
        else:
            non_prime_count[num] += 1

    return reversed_arr, non_prime_count