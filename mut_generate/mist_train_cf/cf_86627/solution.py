"""
QUESTION:
Create a function named `find_odd_or_smallest_prime` that takes a list of integers `arr` as input and returns the first number that appears an odd number of times. If no number appears an odd number of times, the function should return the smallest prime number in the list. The list can contain negative numbers and the function should handle this case correctly.
"""

def find_odd_or_smallest_prime(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num in arr:
        if frequency[num] % 2 != 0:
            return num

    smallest_prime = None
    for num in arr:
        if is_prime(num):
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num
    return smallest_prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True