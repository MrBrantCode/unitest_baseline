"""
QUESTION:
Find the index of the first prime number greater than 23 in a given array of unique integers in ascending order. The array has 5 to 20 elements and must not be modified. Return the index as a positive integer, or -1 if no such prime number is found.

Function: find_index_of_prime_greater_than_23(arr)
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_index_of_prime_greater_than_23(arr):
    index = -1
    for i, num in enumerate(arr):
        if num > 23 and is_prime(num):
            index = i
            break
    return index